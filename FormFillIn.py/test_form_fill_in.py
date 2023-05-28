from HW_5_5.registration import Registration

from UserData.user import user


def test_form_fill_in(browser_setup):
    registration = Registration()
    registration.open()
    registration.fill_in(user)
    registration.submit()
    registration.check(user)
