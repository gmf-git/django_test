"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import ObtainJSONWebToken

from django_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('apps.system.urls')),
    path('record/', include('apps.notes.urls')),
    re_path(r'^upload/(?P<model>.*)/$', views.UpLoadViewSet.as_view(), name='upload'),
    path('login/', ObtainJSONWebToken.as_view()),
    re_path(r'^media/(?P<path>.*)$', static.serve,
            {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('docs/', include_docs_urls(title='接口文档')),
]
