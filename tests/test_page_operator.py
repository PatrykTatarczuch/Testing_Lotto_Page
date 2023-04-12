import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from container_numbers import test_container_numbers
from correct_numbers import test_correctly_numbers
from decimal_numbers import test_decimal_numbers
from duplicate_numbers import test_duplicates
from high_numbers import test_high_numbers
from letters_alphabet import test_letters
from small_numbers import test_small_numbers
from special_characters import test_special_characters


@pytest.mark.html
class TestLotteryGame:

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.get('http://127.0.0.1:5000')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_container_numbers(self):
        test_container_numbers(self, self.driver)

    def test_correctly_numbers(self):
        test_correctly_numbers(self, self.driver)

    def test_decimal_numbers(self):
        test_decimal_numbers(self, self.driver)

    def test_duplicate_numbers(self):
        test_duplicates(self, self.driver)

    def test_high_numbers(self):
        test_high_numbers(self, self.driver)

    def test_letters_alphabet(self):
        test_letters(self, self.driver)

    def test_small_numbers(self):
        test_small_numbers(self, self.driver)

    def test_special_characters(self):
        test_special_characters(self, self.driver)
