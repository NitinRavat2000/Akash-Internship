"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from testapp import views as testapp_views
from exam import views as exam_views
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('testapp',include('testapp.urls')),
    url('exam',include('exam.urls')),
    url('BRMapp',include('BRMapp.urls')),
    url('travello',include('travello.urls')),
    url('todo_list',include('todo_list.urls')),





    #path('test',exam_views.showTest),
    #path('result',exam_views.showResult),
    #path('about/',testapp_views.about),
    #path('contact/',testapp_views.showcontact),
    #url('^$',testapp_views.greeting),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
