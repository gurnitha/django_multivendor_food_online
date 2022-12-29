# main/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Locals
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # accounts
    path('accounts/', include('app.accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
