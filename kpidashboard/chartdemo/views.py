# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,render_to_response

from chartit import DataPool, Chart

from chartdemo.models import MonthlyWeatherByCity

"""
def index(request):
    context = {'tempobj':'test'}
    return render(request,'chartdemo/index.html',context)
"""
def index(request):
    #start_code
    ds = DataPool(
            series=
            [{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
            'terms': [
            'month',
            'houston_temp', 
            'boston_temp']}
            ])

    cht = Chart(
            datasource = ds, 
            series_options = 
            [{'options':{
            'type': 'line',
            'stacking': False},
            'terms':{
            'month': [
            'boston_temp',
            'houston_temp']
            }}],
            chart_options = 
            {'title': {
            'text': 'Weather Data of Boston and Houston'},
            'xAxis': {
            'title': {
            'text': 'Month number'}}})
    #end_code
    return render_to_response('chartdemo/index.html', {'chart_list': cht,'title':'Basic Plot'})
