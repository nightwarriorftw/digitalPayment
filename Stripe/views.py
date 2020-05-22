import stripe

from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, View



class Home(TemplateView):
    template_name = 'base/base.html'

class Stripe(TemplateView):
    template_name='stripe/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        return context


class StripeCharge(View):
    stripe.api_key=settings.STRIPE_SECRET_KEY
    template_name='stripe/charge.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        charge = stripe.Charge.create(
            amount=request.POST['amount'],
            currency='usd',
            description='demo',
            source=request.POST['stripeToken']
        )
        print(charge)

        return render(request, self.template_name, {})
