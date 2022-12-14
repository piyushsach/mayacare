from django.urls import path,include
from . import views
# from razorpay_integration import urls
from . import views

urlpatterns = [
    # path("razorpay/", include(urls), name="urls"),
    path("home/", views.home, name="home"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
]

