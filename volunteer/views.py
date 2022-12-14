from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TimesheetForm, UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import TimeSheets


# Create your views here.
@login_required(login_url='/login/')
def timesheetView(request): 
    context = {
        'logs': TimeSheets.objects.filter(volunteer=request.user).order_by('-start_time')
    }
    return render(request, 'volunteer/timesheet.html', context)


@login_required(login_url='/login/')
def logTimesheet(request):
    if request.method=='POST':
        form = TimesheetForm(request.POST)
        if form.is_valid():
            log = form.save()
            log.user = request.user
            log.save()
            return redirect('timesheet')
    else:
        form = TimesheetForm()

    context = {
        'form': form,
        'title': 'Add Logs'
    }

    return render(request, 'volunteer/add_logs.html', context)


def registerVolunteer(request):
    if request.method=='POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            messages.success(request, f'Your Account has been created!')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Register'
    }

    return render(request, 'volunteer/register.html', context)
    