import allure
from allure_commons.types import Severity

from pages.registration import Registration
from data.user import user


def allure_decoration_steps(func):

    def wrapper(*args, **kwargs):
        return wrapper(*args, **kwargs)

    return func


@allure.tag("Steps")
@allure.label("owner", "YuliyaShkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Пример UI тестирования в рамках обучения в QAGURU")
@allure_decoration_steps
def test_form_fill_in(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('Валидировать данные в форме'):
        registration.check_filled_in_full_data(user)

