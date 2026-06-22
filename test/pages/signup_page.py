from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname):
        firstname_field = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.ID, "UserProfile_FirstName"))
        )
        """firstname_field.clear()"""
        firstname_field.send_keys(firstname)
    
    def enter_lastname(self, lastname):
        lastname_field = self.driver.find_element(By.ID, "UserProfile_LastName")
        lastname_field.clear()
        lastname_field.send_keys(lastname)

  
    def enter_companyname(self, companyname):
        companyname_field = self.driver.find_element(By.ID, "UserProfile_Company")
        companyname_field.clear()
        companyname_field.send_keys(companyname)


    def enter_phonenumber(self, phonenumber):
        phonenumber_field = self.driver.find_element(By.ID, "UserProfile_Phone")
        phonenumber_field.clear()
        phonenumber_field.send_keys(phonenumber)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "UserProfile_Email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

    def confirm_password(self, password):
        confirm_password_field = self.driver.find_element(By.ID, "ConfirmPassword")
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)

    def click_signup_button(self):
        signup_button = self.driver.find_element(By.CSS_SELECTOR, ".kn-button")
        signup_button.click()
        