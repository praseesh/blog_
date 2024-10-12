from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserRegistrationTestCase(APITestCase):
    def setUp(self):
        # Define the URL for registration
        self.url = reverse('register')  # Make sure to replace with your actual URL name

    def test_user_registration_success(self):
        # Prepare valid data for registration
        valid_data = {
            
            "username": "newuser",
            "email" : "newuser@gmail.com",
            "password": "password123"
        }
        # Perform a POST request to register a new user
        response = self.client.post(self.url, valid_data, format='json')

        # Check if the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User Registration Successful')

    def test_user_registration_invalid(self):
        # Prepare invalid data (e.g., missing password)
        invalid_data = {
            "username": "newuser",
            "password": ""
        }
        # Perform a POST request with invalid data
        response = self.client.post(self.url, invalid_data, format='json')

        # Check if the response status is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Check if the error contains the 'password' field error
        self.assertIn('password', response.data)