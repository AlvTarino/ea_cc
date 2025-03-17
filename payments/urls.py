from django.urls import path
from .gateways import visa, mtn_momo, airtel_money

app_name = 'payments'

urlpatterns = [
    path('visa/', visa.VisaGateway.process_payment_view,
         name='process_payment_view'),
    # path('mtn-momo/', mtn_momo.process_payment, name='mtn_momo_payment'),
    # path('airtel-money/', airtel_money.process_payment,
    #      name='airtel_money_payment'),
    path('payment-success/', visa.VisaGateway.payment_success_view,
         name='payment_success_view'),
    path(
        'payment-failure/',
        visa.VisaGateway.payment_failure_view,
        name='payment_failure_view'
    ),
]
