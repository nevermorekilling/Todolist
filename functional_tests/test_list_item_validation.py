from functional_tests.base import FunctionalTest
# from unittest import skip
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You've already got this in your list")
        )

    # @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty lit item. She hits Enter on the empty innput box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request,and does not load the list page
        self.wait_for(
            lambda:
            self.browser.find_element_by_css_selector('#id_text:invalid')
        )

        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(
            lambda:
            self.browser.find_element_by_css_selector(
                '#id_text:valid'
            )
        )

        # And she can submit it sucessfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # # The home page refreshes,and there is an error message saying
        # # that list items cannot be blank
        # self.wait_for(
        #     lambda: self.assertEqual(
        #         self.browser.find_element_by_css_selector('.has-error').text,
        #         "You can't have an empty list item")
        # )

        # # She tries again with some text for the item,which now works
        # self.browser.get_item_input_box().send_keys('Buy milk')
        # self.browser.get_item_input_box().send_keys(Keys.ENTER)

        # Perversely,she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again,the browser will not comply
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(
            lambda:
            self.browser.find_element_by_css_selector('#id_text:invalid')
        )

        # # She receives a similar warning on the list page
        # self.wait_for(
        #     lambda: self.assertEqual(
        #         self.browser.find_element_by_css_selector('.has-error').text,
        #         "You can't have an empty list item")
        # )

        # And she cann correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(
            lambda:
            self.browser.find_element_by_css_selector(
                '#id_text:valid'
            )
        )

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
