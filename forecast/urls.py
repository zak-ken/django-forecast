from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^login/$', login, {'template_name': 'forecast/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'forecast/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profilepage'),
    url(r'^profile/ajax/get_graph_data/$', views.get_graph_data, name='get_graph_data'),
    url(r'^weather_records/$', views.weather_list),
]
