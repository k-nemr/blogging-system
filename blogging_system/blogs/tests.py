import json

from django.test import Client, TestCase
# initialize the APIClient app
from django.urls import reverse
from rest_framework import status

from blogs.models import Blog
from blogs.serializers import BlogSerializer

# Create your tests here.

client = Client()


class list_blogs_test(TestCase):
    """ Test module for list all blogs API """

    def setUp(self):
        Blog.objects.create(author="author 1", subject="subject 1", body="body 1")
        Blog.objects.create(author="author 2", subject="subject 2", body="body 2")
        Blog.objects.create(author="author 3", subject="subject 3", body="body 3")
        Blog.objects.create(author="author 4", subject="subject 4", body="body 4")

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('list_blogs'))
        # get data from db
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class create_blog_test(TestCase):
    """ Test module for create a new blog """

    def setUp(self):
        self.valid_payload = {
            "author": "Author 1",
            "subject": "Subject 1",
            "body": "Body 1"
        }
        self.invalid_payload = {
            'author': '',
            "subject": "Subject 2",
            "body": "Body 2"
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('create_blog'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('create_blog'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
