from django.urls import path
from . import views


urlpatterns = [
    path('', views.SearchForZoneInformation.as_view())
]
