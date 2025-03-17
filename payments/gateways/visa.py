# visa.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.conf import settings


class VisaGateway:
    @staticmethod
    def process_payment(self, amount, card_details):
        headers = {
            'Authorization': f'Bearer {settings.VISA_API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            'amount': amount,
            'card_number': card_details['number'],
            'expiry': card_details['expiry'],
            'cvv': card_details['cvv']
        }
        response = requests.post(
            settings.VISA_API_URL,
            json=payload,
            headers=headers
        )
        return response.json()

    def refund_payment(self, transaction_id):
        headers = {
            'Authorization': f'Bearer {settings.VISA_API_KEY}',
            'Content-Type': 'application/json'
            }
        response = requests.post(
            f'{settings.VISA_API_URL}/{transaction_id}/refund',
            headers=headers
        )
        return response.json()

    def check_payment_status(self, transaction_id):
        headers = {
            'Authorization': f'Bearer {settings.VISA_API_KEY}',
            'Content-Type': 'application/json'
        }
        response = requests.get(
            f'{settings.VISA_API_URL}/{transaction_id}',
            headers=headers
        )
        return response.json()

    # View functions

    def process_payment_view(request):
        if request.method == 'POST':
            # Get payment data from session or request
            gateway = VisaGateway()
            result = gateway.process_payment(
                amount=request.session['amount'],
                card_details={
                    'number': request.POST.get('card_number'),
                    'expiry': request.POST.get('expiry'),
                    'cvv': request.POST.get('cvv')
                }
            )
            if result['status'] == 'approved':
                return redirect('payment_success')
            return redirect('payment_failure')
        return render(request, 'payments/visa.html')

    def payment_success_view(request):
        return render(request, 'payments/success.html')

    def payment_failure_view(request):
        return render(request, 'payments/failure.html')

    def refund_payment_view(request, transaction_id):
        gateway = VisaGateway()
        result = gateway.refund_payment(transaction_id)
        return HttpResponse(result)
