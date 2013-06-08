
from django.conf.urls import patterns, url
from report import views

urlpatterns = patterns("",
        url(r"^Dev/$", views.Dev),
        url(r"^FT/(?P<glCode>\w+)/$", views.showTableFT),
        url(r"^FT/(?P<glCode>\w+)/(?P<kpi>\w+%?)/$", views.showTableFT),
        url(r"^Repoos/(?P<glCode>\w+)/$", views.showTableRep),
        url(r"^Repoos/(?P<glCode>\w+)/Repoos/(?P<kpi>\w+%?)/$", views.showTableRep),
                  )

