import random
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_decimal_numbers(self, setup):
    keys_special = ["2,5", "1.2", "49.1", "0.99", "49.00001", "0,9999"]
    for x in range(1, 7):
        key_element = self.driver.find_element(By.NAME, f"number{x}")
        key_element.send_keys(keys_special[x - 1])
    self.driver.find_element(By.ID, "submitBtn").click()
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