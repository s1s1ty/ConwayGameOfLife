from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^grids/$', GridList.as_view()),
    url(r'^grids/(?P<pk>[0-9]+)/$', GridDetail.as_view()),
]
