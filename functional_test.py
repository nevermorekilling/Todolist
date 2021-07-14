from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retireve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # unittest.main()

# print('it comes here!')
# browser = webdriver.chrome()
# browser = webdriver.firefox()
#  browser.get('http://localhost:8000')

# she notices the page title and header mention to-do lists
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Edith's hobby is tying
# fly-fishing lures)

# When she hits enter, the page updates , and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item.
# She enter "Use peacock feathers to make a fly" (Edith is very
# methodical)

# The page updates again,and now shows both items on her list

# Edith wonders whether the site will remember her list.
# Then she sees that the site has generated a unique URL for her
# -- ther is some explanatory text to that effect

# She visits that URL - Her to-do list is still there

# Satisfied,sho goes back to sleep
# browser.quit()