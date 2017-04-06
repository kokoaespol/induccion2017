"""InduccionNovatos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from proyecto.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'acertijos', AcertijoViewSet)
router.register(r'tesoro', TesoroViewSet)
router.register(r'medalla', MedallaViewSet)
router.register(r'opcion', OpcionViewSet)
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)


urlpatterns = [
    url(r'^auth-token/',obtain_jwt_token),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^home/$', auth_views.login, {'template_name': 'home.html'}, name='home'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^api/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
