from utils.setup_driver import get_driver
from pages.signup_page import SignupPage


driver = get_driver()

url = "https://nigeria.opendataforafrica.org/sys/login/signup"
print(f"Navigating to {url}...")

driver.get(url)

print(driver.title)
print(driver.current_url)
print(driver.page_source[:1000])

signup_page = SignupPage(driver)
signup_page.enter_firstname("Tolu")
signup_page.enter_lastname("Samuel")
signup_page.enter_email("tolusamuel@gmail.com")
signup_page.enter_companyname("Data Science Nigeria")
signup_page.enter_phonenumber("08012345678")
signup_page.enter_password("password123")
signup_page.confirm_password("password123")
signup_page.click_signup_button()

driver.quit()