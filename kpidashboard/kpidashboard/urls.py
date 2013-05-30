from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from kpidashboard import views
#from views import *
#from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kpidashboard.views.home', name='home'),
    # url(r'^kpidashboard/', include('kpidashboard.foo.urls')),
    
    #login / logout 
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'kpidashboard.views.logout_page'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chartdemo/', include('chartdemo.urls')),
    url(r'^report/', include('report.urls')),
)

