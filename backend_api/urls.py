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
    path('',views.render_home, name='home'),
    path('test2/',views.rendertest2, name='images'),

    path('adminpage/', adminviews.render_thumbnail, name='admin'),

    path('adminpage/adminanimals', adminviews.render_adminanimals, name='animals'),
    path('adminpage/adminanimals/addanimal', adminviews.render_addanimal, name='addanimal'),
    path('adminpage/adminanimals/animaldelete/<int:id_animal>', adminviews.render_animal_delete),
    path('adminpage/adminanimals/animalupdate/<int:id_animal>', adminviews.render_animal_update, name='animalupdate'),

    path('adminpage/adminanimals/adminphotos/<int:id_animal>', adminviews.render_admin_photos, name='adminphotos'),
    path('adminpage/adminanimals/adminphotos/photodelete/<int:id_photo>', adminviews.render_photo_delete, name='photodelete'),

    path('adminpage/adminanimals/selectthumbnail/<int:id_animal>', adminviews.render_select_thumbnail, name='selectthumbnail'),
    path('adminpage/adminanimals/selectthumbnail/change/<int:id_photo>', adminviews.render_change_thumbnail, name='changethumbnail'),

    path('adminpage/adminnews', adminviews.render_adminnews, name='adminnews'),
    path('adminpage/adminnews/newnews', adminviews.render_addnews, name='newnews'),
    path('adminpage/adminnews/newsdelete/<int:id_news>', adminviews.render_news_delete),
    path('adminpage/adminnews/newsupdate/<int:id_news>', adminviews.render_news_update, name='newsupdate'),

    path('adminpage/adminapplications', adminviews.render_adminapplications, name='applications'),
    path('adminpage/adminapplications/appdelete/<int:id_app>', adminviews.render_app_delete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
