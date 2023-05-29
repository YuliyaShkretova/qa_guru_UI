from pages.registration import Registration

from userdata.user import user


def test_form_fill_in(browser_setup):
    registration = Registration()
    registration.open()
    registration.fill_in(user)
    registration.submit()
    registration.check(user)
