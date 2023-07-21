import allure
import pytest

from pages.registration import Registration
from data.user import user, userPhone


def allure_decoration_steps(func):
    def wrapper(*args, **kwargs):
        return wrapper(*args, **kwargs)

    return func


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Полное заполнение и отправка формы")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
@pytest.mark.FullFilled
def test_form_fill_in(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in_name(user) \
            .fill_in_surname(user) \
            .fill_in_gender(user) \
            .fill_in_email(user) \
            .fill_in_mobile(user) \
            .fill_in_date_of_birth(user) \
            .fill_in_hobbies(user) \
            .fill_in_subject(user) \
            .load_picture(user) \
            .fill_in_address(user) \
            .fill_in_full_address(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('Валидировать данные в форме'):
        registration.check_filled_in_full_data(user)


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Частичное заполнение формы")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
@pytest.mark.PartlyFilled
def test_form_partly_fill_in(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in_name(user) \
            .fill_in_surname(user) \
            .fill_in_email(user) \
            .fill_in_mobile(user) \
            .fill_in_gender(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('Валидировать данные в форме'):
        registration.check_data(user.name) \
            .check_data(user.surname) \
            .check_data(user.email) \
            .check_data(user.mobile) \
            .check_data(user.gender.value)


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Валидация количества цифр номера мобильного телефона")
@allure.severity(severity_level='MIDDLE')
@allure_decoration_steps
@pytest.mark.MobileCheck
def test_form_12_dig_phone(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить обязательные поля регистрации с 12 символолами в моб.номере'):
        registration.fill_in_name(userPhone) \
            .fill_in_surname(userPhone) \
            .fill_in_email(userPhone) \
            .fill_in_mobile_12_digits(userPhone) \
            .fill_in_gender(userPhone)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('Проверить, что номер телефона состоит из 10 символов '):
        registration.get_mobile_value(userPhone)


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Проверка возможности закрытия модального окна после успешной регистрации")
@allure.severity(severity_level='HIGH')
@allure_decoration_steps
@pytest.mark.CloseWindow
def test_form_close_window(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in_name(user) \
            .fill_in_surname(user) \
            .fill_in_gender(user) \
            .fill_in_email(user) \
            .fill_in_mobile(user) \
            .fill_in_date_of_birth(user) \
            .fill_in_hobbies(user) \
            .fill_in_subject(user) \
            .load_picture(user) \
            .fill_in_address(user) \
            .fill_in_full_address(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('Закрыть окно регистрации и убедиться, что оно закрыто'):
        registration.close()


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Валидация заполнения обязательных полей input - восклицательный знак")
@allure.severity(severity_level='LOW')
@allure_decoration_steps
@pytest.mark.SignValidation
def test_form_validation_sign(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in_gender(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('На обязательных к заполнению полях input валидация отрабатывает'):
        registration.check_validation_element_sign()


@allure.tag("Steps")
@allure.label("owner", "Yuliya Shkretova")
@allure.feature("Tests for DEMO_QA")
@allure.link("https://demoqa.com/automation-practice-form")
@allure.title("Валидация заполнения обязательных полей input - красные границы")
@allure.severity(severity_level='LOW')
@allure_decoration_steps
@pytest.mark.RedValidation
def test_form_validation_red(setup_browser):
    with allure.step('Открыть страницу регистрации'):
        registration = Registration()
        registration.open()
    with allure.step('Заполнить форму регистрации'):
        registration.fill_in_gender(user)
    with allure.step('Отправить форму'):
        registration.submit()
    with allure.step('На обязательных к заполнению полях input валидация отрабатывает'):
        registration.check_validation_element_red()