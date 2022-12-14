from django.urls import path
from .views import donationsView

urlpatterns = [
    path('donations/',donationsView,name="donations"),
]