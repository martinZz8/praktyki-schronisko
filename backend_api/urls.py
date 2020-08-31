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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from app.view import views, adminviews
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_home, name='home'),
    #     path('send_mail/', views.contact, name='send_mail'),
    path('animals', views.render_animals, name='animals'),
    path('animal/<int:id_animal>', views.render_animal, name="animal"),
    path('animal/app/<int:id_animal>',
         views.render_application, name="app"),

    path('news/', views.render_news, name='news'),
    path('post/<int:id_post>', views.render_post, name="post"),

    path('login/', adminviews.login_page, name='login'),
    path('logout/', adminviews.logout_page, name='logout'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name="accounts/password_change_form.html"),
         name="password_change"),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name="accounts/password_change_done.html"),
         name="password_change_done"),

    path('adminpage/', adminviews.render_thumbnail, name='admin'),

    path('adminpage/adminanimals',
         adminviews.render_adminanimals, name='adminanimals'),
    path('adminpage/adminanimals/addanimal',
         adminviews.render_addanimal, name='addanimal'),
    path('adminpage/adminanimals/animaldelete/<int:id_animal>',
         adminviews.render_animal_delete),
    path('adminpage/adminanimals/animalupdate/<int:id_animal>',
         adminviews.render_animal_update, name='animalupdate'),
    path('adminpage/adminanimals/changestatus/<int:id_animal>',
         adminviews.change_animal_visibility, name='changestatus'),

    path('adminpage/adminanimals/adminphotos/<int:id_animal>',
         adminviews.render_admin_photos, name='adminphotos'),
    path('adminpage/adminanimals/adminphotos/photodelete/<int:id_photo>',
         adminviews.render_photo_delete, name='photodelete'),

    path('adminpage/adminanimals/selectthumbnail/<int:id_animal>',
         adminviews.render_select_thumbnail, name='selectthumbnail'),
    path('adminpage/adminanimals/selectthumbnail/change/<int:id_photo>',
         adminviews.render_change_thumbnail, name='changethumbnail'),

    path('adminpage/adminnews', adminviews.render_adminnews, name='adminnews'),
    path('adminpage/adminnews/newnews',
         adminviews.render_addnews, name='newnews'),
    path('adminpage/adminnews/newsdelete/<int:id_news>',
         adminviews.render_news_delete),
    path('adminpage/adminnews/newsupdate/<int:id_news>',
         adminviews.render_news_update, name='newsupdate'),

    path('adminpage/adminapplications',
         adminviews.render_adminapplications, name='applications'),
    path('adminpage/adminapplications/appdelete/<int:id_app>',
         adminviews.render_app_delete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
