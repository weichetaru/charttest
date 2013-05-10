from django.http import HttpResponse
from django.shortcuts import render,render_to_response 

def home(request):
   context = {'title':'Home'}
   return render(request, 'kpidashboard/home.html',context)


