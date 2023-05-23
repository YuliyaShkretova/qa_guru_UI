from selene.support.shared import browser
from selene import be, have, command

from HW_5_5 import resources


class Registration:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_in_name(self, value):
        browser.element('[id="firstName"]').should(be.blank).type(value)

    def fill_in_surname(self, value):
        browser.element('[id="lastName"]').should(be.blank).type(value)

    def fill_in_email(self, value):
        browser.element('[id="userEmail"]').should(be.blank).type(value)

    def choose_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()

    def fill_in_phone(self, value):
        browser.element('[id="userNumber"]').should(be.blank).type(value)

    def fill_in_birthday(self, year, month, date):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{date}:not(.react-datepicker__day--outside-month)').click()

    def fill_in_int(self, value, option):
        browser.element('[id="subjectsInput"]').should(be.blank).type(value)
        browser.element(f'[id=react-select-2-option-{option}]').double_click()

    def choose_hobbies(self, value):
        browser.element(f'[for="hobbies-checkbox-{value}"]').click()

    def load_image(self, value):
        browser.element('#uploadPicture').set_value(resources.image(value))

    def fill_in_address(self, value):
        browser.element('[id="currentAddress"]').should(be.blank).type(value)

    def choose_address(self, state, city):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('[id="state"]').click()
        browser.element(f'[id="react-select-3-option-{state}"]').click()
        browser.element('[id="city"]').click()
        browser.element(f'[id="react-select-4-option-{city}"]').click()

    def submit(self):
        browser.element('[id="submit"]').perform(command.js.scroll_into_view)
        browser.element('[id="submit"]').press_enter()

    def assert_user_data(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address,
                         state_and_city):
        browser.all('tbody tr').should(have.exact_texts(full_name,
                                                        email,
                                                        gender,
                                                        mobile,
                                                        date_of_birth,
                                                        subjects,
                                                        hobbies,
                                                        picture,
                                                        address,
                                                        state_and_city))
        return self


