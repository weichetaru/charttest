from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
   context = {'title':'Home'}
   return render(request, 'kpidashboard/home.html',context)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
