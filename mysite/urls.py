"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.conf.urls import url, include
from django.contrib import admin
from articles.views import main, contact, excursions, houses, home, list_ex, abchazia, transfer, callback, favorite

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^contact/', contact),
    url(r'^callback/', callback),
    url(r'^abchazia/', abchazia),
    url(r'^transfer/', transfer),
    url(r'^excursion/(\d+)/',excursions),
    url(r'^excursions/',list_ex),
    url(r'^house/',houses),
    url(r'^home/(\d+)',home),
    url(r'^favorite/',favorite),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)