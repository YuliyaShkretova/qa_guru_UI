from selene.support.shared import browser
from selene import be, have, command

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

    def fill_in_date_of_birth(self, user: User):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element(f'.react-datepicker__day--0{user.date}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_in_subject(self, user: User):
        for user.subject in user.subject:
            browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def fill_in_hobbies(self, user: User):
        for user.hobbies in user.hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies.value)).click()
        return self

    def load_picture(self, user: User):
        browser.element('#uploadPicture').set_value(resources.image(user.picture))
        return self

    def fill_in_address(self, user: User):
        browser.element('[id="currentAddress"]').type(user.address)
        return self

    def fill_in_full_address(self, user: User):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()
        # browser.element('#submit').execute_script('element.click()')
        return self

    def submit(self):
        browser.element('[id="submit"]').press_enter()
        return self

    def check_filled_in_full_data(self, user: User):
        browser.all('tbody tr').should(have.exact_texts(f'Student Name' + ' ' + user.name + ' ' + user.surname,
                                                        f'Student Email' + ' ' + user.email,
                                                        f'Gender' + ' ' + f'{user.gender.value}',
                                                        f'Mobile' + ' ' + user.mobile,
                                                        f'Date of Birth' + ' ' + f'{user.date}' + ' ' + f'{user.month}' + ',' + f'{user.year}',
                                                        f'Subjects' + ' ' + user.subject,
                                                        f'Hobbies' + ' ' + user.hobbies,
                                                        f'Picture' + ' ' + user.picture,
                                                        'Address' + ' ' + user.address,
                                                        f'State and City' + ' ' + user.state + ' ' + user.city))
        return self

    def check_data(self, value):
        browser.element('.table-responsive').should(have.text(value))
        return self
