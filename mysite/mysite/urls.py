from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from core import views as core_views


urlpatterns = [
	url(r'^admin/?', admin.site.urls),
	url(r'^$', core_views.homepage, name='homepage'),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^about/$', core_views.about, name='about'),
    
]

