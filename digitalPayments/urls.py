from django.urls import path, include
from django.contrib import admin

from Stripe.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('stripe/', include('Stripe.urls', namespace='Stripe')),
]
