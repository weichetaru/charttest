from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from chartit import DataPool, Chart
from chartdemo.models import MonthlyWeatherByCity


@login_required

def home(request):
    #start_code
    df_options ={
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
    'text': 'Month number'}}}
    ds = DataPool(
        series=
        [{'options': {
        'source': MonthlyWeatherByCity.objects.all()},
        'terms': [
        'month',
        'houston_temp',
        'boston_temp']}
        ])

    cht1 = Chart(
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
        chart_options = df_options
        )
    cht2 = Chart(
        datasource = ds,
        series_options =
        [{'options':{
        'type': 'bar',
        'stacking': False},
        'terms':{
        'month': [
        'boston_temp',
        'houston_temp']
        }}],
        chart_options = df_options
        )
    cht3 = Chart(
        datasource = ds,
        series_options =
        [{'options':{
        'type': 'area',
        'stacking': False},
        'terms':{
        'month': [
        'boston_temp',
        'houston_temp']
        }}],
        chart_options = df_options
        )
    cht4 = Chart(
        datasource = ds,
        series_options =
        [{'options':{
        'type': 'column',
        'stacking': False},
        'terms':{
        'month': [
        'boston_temp',
        'houston_temp']
        }}],
        chart_options = df_options
        )
    cht5 = Chart(
        datasource = ds,
        series_options =
        [{'options':{
        'type': 'pie',
        'stacking': False},
        'terms':{
        'month': [
        'boston_temp',
        'houston_temp']
        }}],
        chart_options = df_options
        )
    cht6 = Chart(
        datasource = ds,
        series_options =
        [{'options':{
        'type': 'scatter',
        'stacking': False},
        'terms':{
        'month': [
        'boston_temp',
        'houston_temp']
        }}],
        chart_options = df_options
        )
    #end_code
    return render_to_response('kpidashboard/home.html', {'chart_list': [cht1,cht2,cht3,cht4,cht5,cht6],'title':'Basic Plot'})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
