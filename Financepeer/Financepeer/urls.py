import django
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('api/auth/',include('rest_framework.urls')),
    path('accounts/',include('home.urls')),

]+ static(settings.MEDIA_URL,docment_root = settings.MEDIA_ROOT)
