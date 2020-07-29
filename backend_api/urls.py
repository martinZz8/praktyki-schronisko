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
from django.urls import path
from app import views, adminviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.render_base, name='base'),
    path('test2/',views.rendertest2, name='images'),
    path('adminpage/', adminviews.render_thumbnail, name='admin'),
    path('adminpage/adminanimals', adminviews.admin_animal_retrieve, name='animals'),
    path('adminpage/adminnews', adminviews.admin_news_retrieve, name='adminnews'),
    path('adminpage/adminnews/newnews', adminviews.new_news, name='newnews'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
