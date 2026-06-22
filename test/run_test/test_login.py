from utils.setup_driver import get_driver
from pages.signup_page import LoginPage


driver = get_driver()

url = "https://nigeria.opendataforafrica.org/sys/login"
print(f"Navigating to {url}...")

driver.get(url)

print(driver.title)
print(driver.current_url)
print(driver.page_source[:1000])

login_page = LoginPage(driver)
login_page.enter_email("tolusamuel@gmail.com")
login_page.enter_password("password123")
login_page.click_login_button()

driver.quit()
