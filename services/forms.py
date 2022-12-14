from django.forms.models import ModelForm
from .models import Beneficiary, Service


class BeneficiaryForm(ModelForm):
    class Meta:
        model = Beneficiary
        exclude = []

    def __init__(self, *args, **kwargs):
        super(BeneficiaryForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['volunteer_id', 'beneficiary_id']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})