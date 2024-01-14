from django.test import TestCase
from django.urls import reverse
from users.models import User, UsedToken
from distrigate.security import generate_jwt_token, whitelist_tokens_from_user, require_token
from django.conf import settings
from django.http import JsonResponse
import jwt
import json
from django.contrib.auth import authenticate

class UsersAPITest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # test cases ...
    def test_login_endpoint(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('users:login'), data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json())

    

    def test_get_users_endpoint(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:get_users'))
        self.assertEqual(response.status_code, 200)
        # Add further assertions for the get_users endpoint


    def test_get_user_endpoint(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:get_user', kwargs={'username': 'testuser'}))
        self.assertEqual(response.status_code, 200)
        # Add further assertions for the get_user endpoint


    def test_get_private_user_endpoint(self):

        authenticated = authenticate(username='testuser', password='testpassword')
        self.client.login(username=authenticated.get_username(), password='testpassword')
        token = generate_jwt_token(authenticated.get_username())
        
        response = self.client.get(reverse('users:get_private_user', kwargs={'username': 'testuser'}), HTTP_AUTHORIZATION=f'Bearer {token}')
        
        self.assertEqual(response.status_code, 200)
        # Add further assertions for the get_user endpoint


    def test_generate_jwt_token(self):
        token = generate_jwt_token('testuser')
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded_token['user_id'], 'testuser')
        # Add further assertions for token contents and expiration
        

    def test_whitelist_tokens_from_user(self):
        # Create some used tokens for the test user
        UsedToken.objects.create(access_token='test_token_1', owner=self.user)
        UsedToken.objects.create(access_token='test_token_2', owner=self.user)

        whitelist_tokens_from_user(self.user)

        tokens_count = UsedToken.objects.filter(owner=self.user).count()
        self.assertEqual(tokens_count, 0)
        # Add further assertions for other conditions after whitelisting


    def test_require_token_decorator(self):
        # Assuming require_token is used as a decorator on a dummy view function
        @require_token
        def dummy_view(request):
            return JsonResponse({"message": "Test response"})

        request = self.client.get('/dummy-url/') 
        response = dummy_view(request)
        self.assertEqual(response.status_code, 401)
        # Add further assertions for other scenarios covered by require_token decorator


    def test_logout_endpoint(self):
        authenticated = authenticate(username='testuser', password='testpassword')
        self.client.login(username=authenticated.get_username(), password='testpassword')
        token = generate_jwt_token(authenticated.get_username())

        dummy_body = {
            'username': authenticated.get_username()
        }
        response = self.client.post(reverse('users:logout'), HTTP_AUTHORIZATION=f'Bearer {token}', data=dummy_body, content_type='application/json')
     
        self.assertEqual(response.status_code, 200)
        # Add further assertions for the logout endpoint
