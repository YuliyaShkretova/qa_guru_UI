import time

from selene.support.shared import browser
from selene import be, have, command, query

from data.user import User, Hobbies
from utils import resources, helper


class Registration:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        helper.remove_ads(amount=3, timeout=6)
        helper.remove_ads(amount=1, timeout=2)

    def fill_in_name(self, user: User):
        browser.element('[id="firstName"]').type(user.name)
        return self

    def fill_in_surname(self, user: User):
        browser.element('[id="lastName"]').type(user.surname)
        return self

    def fill_in_email(self, user: User):
        browser.element('[id="userEmail"]').type(user.email)
        return self

    def fill_in_gender(self, user: User):
        browser.all('[name=gender]').element_by(have.value(user.gender.value)).element('..').click()
        return self

    def fill_in_mobile(self, user: User):
        browser.element('[id="userNumber"]').type(user.mobile)
        return self

    def fill_in_mobile_12_digits(self, userPhone: User):
        browser.element('[id="userNumber"]').type(userPhone.mobile)
        return self

    def fill_in_date_of_birth(self, user: User):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element(f'.react-datepicker__day--0{user.date}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_in_subject(self, user: User):
        browser.element('#subjectsInput').type(user.subject.value).press_enter()
        return self

    def fill_in_hobbies(self, user: User):
        # browser.all('.custom-control-label').perform(command.js.scroll_into_view)
        browser.all('.custom-control-label').element_by(have.exact_text(user.hobbies.value)).click()
        return self

    def load_picture(self, user: User):
        browser.element('#uploadPicture').set_value(resources.image(user.picture))
        return self

    def fill_in_address(self, user: User):
        browser.element('[id="currentAddress"]').type(user.address)
        return self

    def fill_in_full_address(self, user: User):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()
        return self

    def submit(self):
        browser.element('[id="submit"]').press_enter()
        return self

    def close(self):
        browser.element('[id="closeLargeModal"]').perform(command.js.scroll_into_view).click()
        browser.element('[id="closeLargeModal"]').should(be.not_.visible)
        return self

    def check_filled_in_full_data(self, user: User):
        browser.all('tbody tr').should(have.exact_texts(f'Student Name' + ' ' + user.name + ' ' + user.surname,
                                                        f'Student Email' + ' ' + user.email,
                                                        f'Gender' + ' ' + f'{user.gender.value}',
                                                        f'Mobile' + ' ' + user.mobile,
                                                        f'Date of Birth' + ' ' + f'{user.date}' + ' ' + f'{user.month}' + ',' + f'{user.year}',
                                                        f'Subjects' + ' ' + f'{user.subject.value}',
                                                        f'Hobbies' + ' ' + f'{user.hobbies.value}',
                                                        f'Picture' + ' ' + user.picture,
                                                        'Address' + ' ' + user.address,
                                                        f'State and City' + ' ' + user.state + ' ' + user.city))
        return self

    def check_data(self, value):
        browser.element('.table-responsive').should(have.text(value))
        return self

    def get_mobile_value(self, userPhone: User):
        mob1 = userPhone.mobile[:-2]
        browser.element('tr:nth-child(4) > td:nth-child(2)').should(have.exact_text(mob1))


    def check_validation_element_sign(self):
        fist_name_sign = browser.element('[id="firstName"]').get(query.css_property('background-image'))
        last_name_sign = browser.element('[id="lastName"]').get(query.css_property('background-image'))
        phone_number_sign = browser.element('[id="userNumber"]').get(query.css_property('background-image'))
        fist_name_border = browser.element('[id="firstName"]').get(query.css_property('border-color'))
        last_name_border = browser.element('[id="lastName"]').get(query.css_property('border-color'))
        phone_number_border = browser.element('[id="userNumber"]').get(query.css_property('border-color'))
        assert fist_name_sign, last_name_sign and phone_number_sign is not None
        assert fist_name_border, last_name_border and phone_number_border == 'dc3545'
        return self