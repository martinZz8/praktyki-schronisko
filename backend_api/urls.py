"""backend_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app.view import views, adminviews
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.render_base, name='base'),
    path('test2/',views.rendertest2, name='images'),
    path('adminpage/', adminviews.render_thumbnail, name='admin'),
    path('adminpage/adminanimals', adminviews.render_adminanimals, name='animals'),
    path('adminpage/adminnews', adminviews.render_adminnews, name='adminnews'),
    path('adminpage/adminnews/newnews', adminviews.render_addnews, name='newnews'),
    path('adminpage/adminnews/render_news_delete/<int:id_news>', adminviews.render_news_delete),
    path('adminpage/adminnews/newsupdate/<int:id_news>', adminviews.render_news_update, name='newsupdate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
