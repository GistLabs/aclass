from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse, path, include
from todo.models import Todo


# Define this after the ModelTestCase
class ViewTestCase(APITestCase):
    """Test suite for the api views."""

    def test_api_can_create_a_todo(self):
        """Test the api has bucket creation capability."""
        todo_data = {'title': 'Go to Ibiza and buy fudge',
                     'description': 'Ibiza todo', 'completed': False}
        response = self.client.post('/api/todos/', todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        get_response = self.client.get('/api/todos/1/')

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            get_response.data['title'], 'Go to Ibiza and buy f*dge')
