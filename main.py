import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class SignUpTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://politrip.com/account/sign-up')
        self.assertIn('Sign up | Politrip', self.browser.title)

    def test_sign_up(self):
        def fill_field(id,text):
            element = self.browser.find_element(By.ID, id)
            element.send_keys(text)

        self.browser.get('https://politrip.com/account/sign-up')
        time.sleep(3)
        cookies = self.browser.find_element(By.ID, 'cookiescript_accept')
        cookies.click()
        fill_field('first-name','Andreea')
        fill_field('last-name','Jicmon')
        fill_field('email','andreea.jicmon@student.tuiasi.ro')
        fill_field('sign-up-password-input','Internship123')
        fill_field('sign-up-confirm-password-input','Internship123')

        sign_up = self.browser.find_element(By.XPATH, '//*[@id=" qa_loader-button"]')
        self.browser.execute_script("arguments[0].click();", sign_up)

        time.sleep(3)
        self.assertIn('https://politrip.com/account/sign-up/type-select', self.browser.current_url)

if __name__ == "__main__":
    unittest.main()