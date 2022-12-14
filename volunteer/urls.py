from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('volunteer/', volunteerView, name="volunteer"),
    path('timesheet/', timesheetView, name="timesheet"),
    path('add_logs/', logTimesheet, name="add_logs"),
    path('register/', registerVolunteer, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='volunteer/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/log_out.html'), name='logout'),
]