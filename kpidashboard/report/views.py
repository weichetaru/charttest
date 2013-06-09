# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import os,re
from django.conf import settings
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
import MySQLdb

"""
def buildContents(files):
    f = open(files)
    contents = ""
    cnt = 0
    for line in f:
        if line.startswith(('<tr','<td')):
            cnt +=1
            if cnt == 1:
                line = "<thead> "+line
            if cnt == 2:
                line = line.replace("td>","th class='header'>")
                line = line + " </thead> <tbody>"
            if line.find('%') >0:
                line = re.sub(r'(\d+\.\d+)', r"\1 %", line)
            else:
                line = line.replace('.00','')
            contents += line
    f.close()
    return contents.decode("shift-jis") +" </tbody>"
"""

showList=["total_ft%","ft_retail%","ft_fba%","ctrl%","x3p_ctrl%","x3p_non_ctrl%","nofr%","total_ft","ft_retail","ft_fba","ctrl","x3p_ctrl","x3p_non_ctrl","nofr","total_glance_view"]

def isnum(x):
    import locale
    locale.setlocale(locale.LC_NUMERIC, 'ja_JP')
    if x is None:
        return str(x)
    try:
        x = 1*x
        return locale.format('%.2f', x, True)
    except:
        return x

def buildContents(dbname,ajax=0):
    sqlHead = "SELECT column_name FROM information_schema.columns WHERE table_name= '%s' ;" % dbname
    headertmp = get_data_from_db(sqlHead)
    header = [tp[0] for tp in headertmp ]
    sqlBody = "SELECT %s FROM `%s` ;" % (",".join(header),dbname)
    body = get_data_from_db(sqlBody)
    #date var 
    header = [re.sub(r'^X(\d{4})_(\d{2})_(\d{2}$)', r"\1/\2/\3", tp) for tp in header]
    headerHtml = "<thead><tr><th class = 'header' >" + "</th> <th class='header'>".join(header) + "</tr> </thead>"
    contents = ""
    for raw in body:
        line = ""
        for inline in raw:
            line += "<td>" + isnum(inline) + "</td>"
        line = "<tr>" + line + "</tr>"
        if line.find('%') >0:
            line = re.sub(r'(\d+\.\d{1,2})</td>', r"\1 %", line)
        else:
            line = line.replace('.00','')
        contents += line
    bodyHtml = "<tbody>" + contents + "</tbody>"
    return headerHtml +bodyHtml
    #return headerHtml.decode("utf8") +bodyHtml.decode("utf8") 
    #return body 

def get_data_from_db(sql, usedb="report"):
    in_db=usedb
    in_host="localhost"
    in_port=3306
    in_user="dbuser"
    in_pass="dbuser"
    in_con = MySQLdb.connect(db=in_db,  host=in_host, port=in_port,user=in_user,passwd=in_pass, charset='utf8')
    cur = in_con.cursor()
    cur.execute(sql)
    result_lst = cur.fetchall()
    cur.close()
    in_con.commit()
    in_con.close()
    return result_lst


def Dev(request):
    data = buildContents('dsKpiDetail_ft_fba_6_Jewelry')
    return HttpResponse(data)

def showTableFT(request,glCode,kpi = "total_ft%",mklist = ['6','41092']):
    contentsDic={
            'dsKpiTopC' : {},
            'dsKpiTopB' : {},
            'dsKpiDetail' : {},
            'ftResultall' : {}
    }
    if request.is_ajax():
        mkid = request.GET['mklist']
        byItem = request.GET['byItem']
        for key in ['dsKpiTop'+byItem,'dsKpiDetail']:
            path0=key+"_" +kpi + "_" + mkid + "_" + glCode
            addHeader = '<table id="top%s%s" class = "table table-bordered table-hover table-condensed tablesorter">' % (byItem,str(mkid)) 
            try:
                contentsDic[key][mkid] = addHeader + buildContents(path0) + '</table>'
            except:
                contentsDic[key][mkid] = "<h4 class='text-error'>No Data <h4>"

        return HttpResponse(simplejson.dumps({'top' :
            contentsDic['dsKpiTop'+byItem], 
            'detail' : contentsDic['dsKpiDetail'],'KPI' :kpi},ensure_ascii=False), content_type=u'application/json')
    else:
        for mkid in mklist:
            for key in contentsDic:
                if key == 'ftResultall':
                    path0=key+ "_" + mkid + "_" + glCode
                else:
                    path0=key+"_" +kpi + "_" + mkid + "_" + glCode
                try:
                    contentsDic[key][mkid] = buildContents(path0)
                except:
                    contentsDic[key][mkid] = "<h4 class='text-error'>No Data <h4>"

        return render_to_response('report/reportFt.html',{'all'
            :contentsDic['ftResultall'],'topC' : contentsDic['dsKpiTopC'],'topB'
            : contentsDic['dsKpiTopB'], 'detail' :contentsDic['dsKpiDetail'],'GL' : glCode,'KPI' : kpi, 'showList':showList })


def showTableRep(request,glCode,kpi = "repoos"):
    contentsDic={
            'dsKpiRepBrand' : {},
            'dsKpiRepASIN' : {},
    }
    for key in contentsDic:
        path0=key + "_" + glCode
        try:
            contentsDic[key] = buildContents(path0)
        except:
            contentsDic[key] = "<h4 class='text-error'>No Data <h4>"
    return render_to_response('report/reportRep.html',
            {'brand' : contentsDic['dsKpiRepBrand'],'asin' : contentsDic['dsKpiRepASIN'], 'GL' : glCode,'KPI' : kpi})

