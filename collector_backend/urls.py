"""
URL configuration for collector_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from messaging import views as messaging_views
from account import views as account_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # Initial redirect
    path('', account_views.account, name='account'),
    
    # Sign up
    path('account/signup/', account_views.signup, name='signup'),

    # Log in
    path('account/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),

    # Messaging
    path('messages/', messaging_views.index, name='messages'),
    path('messages/<str:handle>/', messaging_views.chat_room, name='chat'),

    # Admin and other routes
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('userCollections.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
