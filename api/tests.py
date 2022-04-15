from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class TestCaseBase(APITestCase):
    @property
    def bearer_token(self):
        user = User.objects.create_user(
            username='test_user', password='12345678'
        )

        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class PostsTestClass(TestCaseBase):

    url = reverse('posts')

    def test_get_list_no_auth(self):
        self.client.login(username='test_user', password='t12345678')
        data = {
                'title': 'test title',
                'text': 'test_text'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)