from django.conf.urls import patterns, url

from chartdemo import views

urlpatterns = patterns("",
    url(r"^$", views.index, name='index')
)