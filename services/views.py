from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BeneficiaryForm, ServiceForm

# Create your views here.
def servicesView(request):
    if request.method=='POST':
        beneficiary_form = BeneficiaryForm(request.POST)
        service_form = ServiceForm(request.POST)
        if beneficiary_form.is_valid() and service_form.is_valid():
            beneficiary = beneficiary_form.save()
            service = service_form.save()
            service.beneficiary_id = beneficiary
            service.save()
            messages.success(request, f'Your Request is Sent!')
            return redirect('services')
    else:
        beneficiary_form = BeneficiaryForm()
        service_form = ServiceForm()

    context = {
        'beneficiary_form': beneficiary_form,
        'service_form': service_form,
        'title': 'Register'
    }

    return render(request, 'services/services.html', context)
