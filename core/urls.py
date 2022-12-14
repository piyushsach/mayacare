from django.urls import path
from .views import lmsView, welcomeView, dashboardView

urlpatterns = [
    path('', welcomeView, name="welcome"),
    path('dashboard/', dashboardView, name="dashboard"),
    path('lms/', lmsView, name="lms"),
]