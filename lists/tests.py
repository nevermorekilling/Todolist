from django.test import TestCase
# from django.template.loader import render_to_string
# from django.urls import resolve
# from django.http import HttpRequest, request
# from lists.views import home_page
from lists.models import Item, List
# Create your tests here.


class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_itemsj(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 4)


class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new',
                                    data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

        # <Sth Personal>
        # Digitalization is the first step of this world!!!
        # you got to know what kind of thing you are trying to do,
        # and understand it in a digital way,
        # time has changed so much.

        # # getting redirected
        # self.assertEqual(response.status_code, 302)
        # # self.assertEqual(response['location'], '/')
        # self.assertEqual(response['location'],
        #                  '/lists/the-only-list-in-the-world')


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        # watch out the ending "/" !!!
        # if you do not use the slash it will automatically redirect you to
        # a URL using slash!!!
        # 301はWebサイトが移転し、新サイトにリダイレクトされた場合などに用いられます。
        # また、URLの末尾に「/」をつけずにアクセスした場合も、自動的に「/」がついたサイトへ遷移するため
        # 「301 Moved Permanently」となることがあります。
        # response = self.client.get('/lists/the-only-list-in-the-world')
        response = self.client.get('/lists/the-only-list-in-the-world/')
        # print(response.url, '+++', response.status_code)

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class HomePageTest(TestCase):

    # home_page no longer handle post related things remove test method
    # def test_only_saves_items_when_necessary(self):
    #     self.client.get('/')
    #     self.assertEqual(Item.objects.count(), 0)

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

    # def test_home_page_returns_correct_html(self):
    #     response = self.client.get('/')
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')

        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, expected_html)

        # self.assertTemplateUsed(response, 'home.html')

        # self.assertTemplateUsed(response, 'wrong.html')
