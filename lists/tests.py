from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import resolve
from django.http import HttpRequest, request
from lists.views import home_page

# Create your tests here.


# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 4)


class HomePageTest(TestCase):
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')

        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, expected_html)

        self.assertTemplateUsed(response, 'home.html')

        # self.assertTemplateUsed(response, 'wrong.html')
