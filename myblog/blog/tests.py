import unittest
from django.test import TestCase
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser', password='password')

    def tearDown(self):
        self.user.delete()

    def test_add_blog_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/admin/blog/blog/add/', {'title': 'My test title', 'body': 'My test body', '_save': 'SAVE'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertTrue('My test title' in str(response.content))

    def test_delete_blog_post(self):
        self.client.login(username='testuser', password='password')
        self.client.post('/admin/blog/blog/add/', {'title': 'Title to delete', 'body': 'Body to delete', '_save': 'SAVE'})
        response = self.client.get('/')
        self.assertTrue('Title to delete' in str(response.content))
        response = self.client.get('/admin/blog/blog/1/delete/', )
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Are you sure you want to delete the blog' in str(response.content))
        response = self.client.post('/admin/blog/blog/2/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse('Title to delete' in str(response.content))
        print(response.context)