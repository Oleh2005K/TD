from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    URL = 'https://example.com/register'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локатори полів
    username_input: WebElement = (By.ID, 'username')
    email_input:    WebElement = (By.ID, 'email')
    password_input: WebElement = (By.ID, 'password')
    confirm_input:  WebElement = (By.ID, 'confirmPassword')
    submit_button:  WebElement = (By.CSS_SELECTOR, 'button[type=submit]')

    def load(self):
        self.driver.get(self.URL)

    def register(self, username: str, email: str, password: str):
        self.wait.until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self) -> str:
        msg_locator = (By.CLASS_NAME, 'success-message')
        return self.wait.until(EC.visibility_of_element_located(msg_locator)).text