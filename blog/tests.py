from django.test import TestCase
from django.shortcuts import reverse

from .models import Post

# Create your tests here.


class BlogPostListViewTest(TestCase):
    # برو داخل صفحه اصلی و بررسی کن درست کار میکنه یا نه
    # بره به یو ار ال خالی

    def test_posts_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # تست name=home در url
    def test_posts_list_view_by_url_name(self):
        response1 = self.client.get(reverse('home'))
        self.assertEqual(response1.status_code, 200)



