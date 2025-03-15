# test for payments
from django.test import TestCase
from payments.gateways.visa import VisaGateway
from unittest.mock import patch


class PaymentGatewayTests(TestCase):
    @patch('requests.post')
    def test_visa_payment_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'status': 'approved'}
        gateway = VisaGateway()
        response = gateway.process_payment(100, {
            'number': '4111111111111111',
            'expiry': '12/25',
            'cvv': '123'
        })
        self.assertEqual(response['status'], 'approved')
