from django.http import HttpResponse
from django.shortcuts import render,render_to_response
import os,re
from django.conf import settings
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

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

showList=["total_ft%","ft_retail%","ft_fba%","ctrl%","_3p_ctrl%","_3p_non_ctrl%","nofr%","total_ft","ft_retail","ft_fba","ctrl","_3p_ctrl","_3p_non_ctrl","nofr","total_glance_view"]

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
            path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode+"/"+key+"_" +kpi + "_" + mkid + "_" + glCode + ".html")
            try:
                contentsDic[key][mkid] = buildContents(path0)
            except:
                contentsDic[key][mkid] = "<h4 class='text-error'>No Data <h4>"

        return HttpResponse(simplejson.dumps({'top' :
            contentsDic['dsKpiTop'+byItem], 
            'detail' : contentsDic['dsKpiDetail'],'KPI' :kpi},ensure_ascii=False), content_type=u'application/json')
    else:
        for mkid in mklist:
            for key in contentsDic:
                if key == 'ftResultall':
                    path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" +glCode+"/"+key+"_all" + "_" + mkid + "_" + glCode + ".html")
                else:
                    path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode+"/"+key+"_" +kpi + "_" + mkid + "_" + glCode + ".html")
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
        path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode+"/"+key + "_" + glCode + ".html")
        try:
            contentsDic[key] = buildContents(path0)
        except:
            contentsDic[key] = "<h4 class='text-error'>No Data <h4>"
    return render_to_response('report/reportRep.html',
            {'brand' : contentsDic['dsKpiRepBrand'],'asin' : contentsDic['dsKpiRepASIN'], 'GL' : glCode,'KPI' : kpi})

