from django.urls import path
from .views import Stripe, StripeCharge


app_name='Stripe'

urlpatterns = [
    path('', Stripe.as_view(), name='Stripe'),
    path('charge/', StripeCharge.as_view(), name='stripeCharge'),
]