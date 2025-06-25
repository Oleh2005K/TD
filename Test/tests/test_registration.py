import pytest
from pages.registration_page import RegistrationPage

@ pytest.mark.smoke
def test_successful_registration(driver):
    reg_page = RegistrationPage(driver)
    reg_page.load()
    # Унікальні дані можна генерувати динамічно
    username = 'user_' + str(int(pytest.time.time()))
    email = f"{username}@example.com"
    password = 'SecurePass123!'

    reg_page.register(username, email, password)
    success_text = reg_page.get_success_message()
    assert 'Дякуємо за реєстрацію' in success_text