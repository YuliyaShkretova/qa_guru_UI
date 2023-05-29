from pages.registration import Registration
from userdata.user import user


def test_form_fill_in(setup_browser):
    browser = setup_browser
    registration = Registration(browser)
    registration.open()
    registration.fill_in(user)
    registration.submit()
    registration.check(user)
