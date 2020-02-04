import unittest
from selenium import webdriver

class FreeLibraryPage(unittest.TestCase):

    base_url = "https://www.oxfordowl.co.uk/library-page"

    search_term="fly"

    #  Test Pre - Condition
    def setUp(self):
       self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

    def test_load_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

        self.assertIn("Free eBook library|Oxford Owl", driver.title)

    def test_search_for_a_search_term(self):
            self.driver.get(self.base_url)
            search_bar = self.driver.find_element_by_name("query")
            search_bar.clear()
            search_bar.send_keys(self.search_term)
            self.assertIn(self.search_term, self.driver.title)
            self.assertNotIn("No results found.", self.driver.page_source)
            self.assertIn(self.search_term, self.driver.title)

            # --- Post - Condition ---
    def tearDown(self):
        # to close the browser
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main()
