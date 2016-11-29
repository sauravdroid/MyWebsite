from django.conf.urls import url
from . import views
app_name = 'pages'
urlpatterns = [
    url(r'^$',views.home_page,name='home'),
    url(r'^about/$',views.about_me_page,name='about'),
    url(r'^projects/$',views.projects_page,name='projects'),
]