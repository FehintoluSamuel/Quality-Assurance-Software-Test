from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "EMail"))
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "Password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input.login")
        login_button.click()