import random
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_small_numbers(self, setup):
    keys_small_list = [1, 1, 1, 1, 1, 1]
    for x in range(1, 7):
        small_key = False
        while not small_key:
            keys_small = random.randint(-100, 0)
            if keys_small not in keys_small_list:
                keys_small_list[x - 1] = keys_small
                key_element = self.driver.find_element(By.NAME, f"number{x}")
                key_element.send_keys(keys_small_list[x - 1])
                small_key = True
    rand_list = []
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
                rand_list.append(rand)

            else:
                continue
        x += 1
    self.driver.find_element(By.ID, "submitBtn").click()
    assert self.driver.find_element(By.ID, "chosen").is_displayed(), "Ta funkcja nie działa"