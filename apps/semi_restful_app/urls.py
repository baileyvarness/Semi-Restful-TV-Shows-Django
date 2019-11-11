from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows/new$', views.shows_new),
    url(r'^add_show$', views.add_show),
    url(r'^show_page/(?P<show_id>\d+)$', views.show_page),
    url(r'^shows$', views.shows),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.show_edit),
    url(r'^edit_show/(?P<show_id>\d+)$', views.edit_show),
    url(r'^delete/(?P<show_id>\d+)$', views.delete)
]