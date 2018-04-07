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
from proyecto import views
from proyecto.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'treasures', TreasureViewSet)
router.register(r'medals', MedalViewSet)
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'blocks', BlockViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'misions', MisionViewSet)
router.register(r'typesR', TypeRViewSet)
router.register(r'typesT', TypeTViewSet)
router.register(r'keysR', KeyRViewSet)
router.register(r'keysT', KeyTViewSet)
router.register(r'misionprofile', MisionProfileViewSet)


urlpatterns = [
    url(r'^auth-token/',obtain_jwt_token),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^home/$', auth_views.login, {'template_name': 'home.html'}, name='home'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^api/', include('rest_framework.urls',namespace='rest_framework')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^', include(router.urls)),
]
