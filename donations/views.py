from django.shortcuts import render

# Create your views here.

def donationsView(request):
    return render(request,'donations/donate.html')

