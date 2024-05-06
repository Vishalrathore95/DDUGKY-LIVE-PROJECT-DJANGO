"""
URL configuration for ddu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

import uuid
from teacher import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.signup),
    path('index/', views.index ,name='index'),
    path('about/', views.about),
    path('canteen/', views.canteen),
    path('canteen/<int:rev>/', views.revi),
    path('contact/', views.contact,name="contact"),
    path('course/', views.course),
  
    path('batches/', views.batches),
    path('batches/<int:bia>', views.bt),
    path('placement/', views.placement),
    path('reset/', views.reset),
    path('review/', views.review,name='review'),
    path('teacher/', views.teacher),  
    path('tsc/', views.tsc),
    path('bia/', views.bia),
   
    path('login/', views.login,name='login'),
    path('login/<int:forgot>/', views.forgot),
    path('logout/', views.logout, name='logout'),
    path('thanks/', views.thanks),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='passworddone.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complate.html'), name='password_reset_complete'),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


