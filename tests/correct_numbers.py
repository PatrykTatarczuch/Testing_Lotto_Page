import random
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_correctly_numbers(self, setup):
    keys = random.sample(range(1, 50), 6)
    for i in range(1, 7):
        unique_key = False
        while not unique_key:
            key = random.randint(1, 49)
            if key not in keys:
                keys[i - 1] = key
                unique_key = True
        number_input = self.driver.find_element(By.NAME, f"number{i}")
        number_input.send_keys(str(keys[i - 1]))
    self.driver.find_element(By.ID, "submitBtn").click()
    chosen_random_numbers = self.driver.find_element(By.ID, "chosen")
    chosen_random_text = chosen_random_numbers.text
    chosen_random_list = [int(x) for x in chosen_random_text.split(":")[1].strip()[1:-1].split(", ")]
    assert str(keys) == str(chosen_random_list), "Wybrane liczby nie zgadzają się z wyświetlonymi"
    assert self.driver.find_element(By.ID, "chosen").is_displayed(), "Ta funkcja nie działa"