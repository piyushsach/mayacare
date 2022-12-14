from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcomeView(request):
    return render(request,'core/welcome.html')

@login_required(login_url='/login/')
def dashboardView(request):
    return render(request, 'core/dashboard.html')

def lmsView(request):
    return render(request,'core/lms.html')


