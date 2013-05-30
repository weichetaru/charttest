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
    return contents+" </tbody>"

showList=["total_ft%","ft_retail%","ft_fba%","ctrl%","_3p_ctrl%","_3p_non_ctrl%","nofr%","total_ft","ft_retail","ft_fba","ctrl","_3p_ctrl","_3p_non_ctrl","nofr","total_glance_view"]

def showTableFT(request,glCode,kpi = "total_ft%",mklist = ['6','41092']):
    contentsTopC = {}
    contentsTopB = {}
    contentsDetail = {}
    contentsAll = {}
    if request.is_ajax():
        contentsTop = {}
        mkid = request.GET['mklist']
        byItem = request.GET['byItem']
        path1=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode + "/dsKpiDetail_" + kpi+"_" + mkid + "_" + glCode + ".html")
        path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode +
                "/dsKpiTop"+byItem+"_" + kpi + "_" + mkid + "_" + glCode + ".html")
        try:
            contentsTop[mkid] = buildContents(path0)
            contentsDetail[mkid] = buildContents(path1)
        except:
            contentsTop[mkid] = "<h4 class='text-error'>No Data <h4>"
            contentsDetail[mkid] = "<h4 class='text-error'>No Data <h4>"
        return HttpResponse(simplejson.dumps({'top' : contentsTop, 
            'detail' : contentsDetail,'KPI' :kpi},ensure_ascii=False), content_type=u'application/json')
    else:
        for mkid in mklist:
            path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode + "/dsKpiTopC_" + kpi + "_" + mkid + "_" + glCode + ".html")
            path1=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode + "/dsKpiDetail_" + kpi+"_" + mkid + "_" + glCode + ".html")
            path2=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode + "/ftResultall_all" + "_" + mkid + "_" + glCode + ".html")
            path3=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode + "/dsKpiTopB_" + kpi + "_" + mkid + "_" + glCode + ".html")
            try:
                contentsTopC[mkid] = buildContents(path0)
                contentsDetail[mkid] = buildContents(path1)
                contentsAll[mkid] = buildContents(path2)
                contentsTopB[mkid] = buildContents(path3)
            except:
                contentsTopC[mkid] = "<h4 class='text-error'>No Data <h4>"
                contentsDetail[mkid] = "<h4 class='text-error'>No Data <h4>"
                contentsAll[mkid] = "<h4 class='text-error'>No Data <h4>"
                contentsTopB[mkid] = "<h4 class='text-error'>No Data <h4>"
        return render_to_response('report/reportFt.html',{'all' : contentsAll,'topC' : contentsTopC,
            'topB' :contentsTopB, 'detail' : contentsDetail,'GL' : glCode,'KPI' : kpi, 'showList':showList })



def showTableRep(request,glCode,kpi = "repoos"):
    contentsBrand = {}
    contentsAsin = {}
    path0=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode +"/dsKpiRepBrand" + "_" + glCode + ".html")
    path1=os.path.join(settings.MEDIA_ROOT, "ftReport/" + glCode +"/dsKpiRepASIN" + "_" + glCode + ".html")
    try:
        contentsBrand = buildContents(path0)
        contentsAsin = buildContents(path1)
    except:
        contentsBrand = "<h4 class='text-error'>No Data <h4>"
        contentsAsin = "<h4 class='text-error'>No Data <h4>"
    return render_to_response('report/reportRep.html',
            {'brand' : contentsBrand,'asin' : contentsAsin, 'GL' : glCode,'KPI' : kpi})

