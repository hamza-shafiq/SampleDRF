"""PheadraDRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve as static_serve
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Dispatch API')

urlpatterns = [
    path('secure-admin/', admin.site.urls),
    path('',  include('info.urls')),
    url(r'sample-drf^$', schema_view),
    path('dispatch-app/', include('dispatch_app.urls')),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', static_serve, {'document_root': settings.STATIC_ROOT}),
]
