import random
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_container_numbers(self, setup):
    rand_list = [0, 0, 0, 0, 0, 0]
    x = 0
    while x <= 5:
        self.driver.find_element(By.ID, "submitBtn").click()
        try:
            if self.driver.find_element(By.ID, "chosen"):
                pytest.fail("element 'chosen' został znaleziony")
        except:
            rand = random.randint(1, 49)
            clearing_buttons = self.driver.find_element(By.NAME, f"number{x + 1}")
            clearing_buttons.clear()
            if rand not in rand_list:
                clearing_buttons.send_keys(rand)
                rand_list[x] = rand
                x += 1
            else:
                continue
    self.driver.find_element(By.ID, "submitBtn").click()
    assert self.driver.find_element(By.ID, "chosen").is_displayed(), "Ta funkcja nie działa"