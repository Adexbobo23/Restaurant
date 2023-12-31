"""
URL configuration for restoran project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pages.views import (
    index,
    about,
    menu,
    service,
    team,
    booking,
    contact,
    testimonial,
    )
from users.views import register, logout_view, login_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('restoran/admin', include('admin_argon.urls')),
    path('admin/', admin.site.urls),
    path('', index, name= 'home'),
    path('about/', about, name= 'about'),
    path('menu/', menu, name= 'menu'),
    path('service/', service, name= 'service'),
    path('team/', team, name= 'team'),
    path('booking/', booking, name= 'booking'),
    path('contact/', contact, name= 'contact'),
    path('testimonial/', testimonial, name= 'testimonial'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)