from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from chartit import DataPool, Chart
from chartdemo.models import MonthlyWeatherByCity


@login_required

def home(request):
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
        {
        'title':{
            'text':'Temp Comparison'
            },   
        'chart': {
            'height':250,
            'borderWidth': 1,
        },   
        'yAxis': {
            'title':{
                'text':' '
                },
            'offset':0
        },   
        'xAxis': {
        'title': {
        'text': 'Month number'}}})
    #end_code
    return render_to_response('kpidashboard/home.html', {'chart_list': cht,'title':'Basic Plot'})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
