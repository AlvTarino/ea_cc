# visa.py
import requests
from django.conf import settings


class VisaGateway:
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
