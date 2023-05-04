"""blog_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog_app import views

admin.site.site_header = "Ajeet Kumar Admin"
admin.site.site_title = "Blog Project Admin Portal"
admin.site.index_title = "Welcome To Blog Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('form',views.form,name='form'),
    path('delete<int:id>',views.delete,name='delete'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('showsign',views.showsign,name='showsign'),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('edit',views.edit,name='edit'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('changep',views.changep,name='changep'),
    path('profileimage',views.profile_image,name='profileimage'),
    path('update<int:id>',views.update,name='update'),







]
