from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    url(r'hours/$', views.HourList.as_view()),
    url(r'hours/(?P<pk>[0-9]+)/$', views.HourDetail.as_view()),
    url(r'^nearby_locations/?$', views.NearbyLocationList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)