from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class UserTestCase(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.
                        filter(username='testuser').exists())

    def test_login(self):
        CustomUser.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)

    def test_profile_access(self):
        CustomUser.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:profile',
                                           kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
