from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.home,name='home'),
    path("save", views.SaveFile, name="save"),
    path("api/auth", views.CustomAuthToken.as_view()),
    path("profile/", views.Userview.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
