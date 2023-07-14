from selene.support.shared import browser
from selene import be, have, command

from data.user import User
from utils import resources, helper


class Registration:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        helper.remove_ads(amount=3, timeout=6)
        helper.remove_ads(amount=1, timeout=2)

    def fill_in(self, user: User):
        browser.element('[id="firstName"]').type(user.name)
        browser.element('[id="lastName"]').type(user.surname)
        browser.element('[id="userEmail"]').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender.value)).element('..').click()
        browser.element('[id="userNumber"]').type(user.mobile)
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element(f'.react-datepicker__day--0{user.date}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element(f'[for="hobbies-checkbox-3"]').click()
        browser.element('#uploadPicture').set_value(resources.image(user.picture))
        browser.element('[id="currentAddress"]').type(user.address)
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('[id="state"]').click()
        browser.element('[id="react-select-3-input"]').type(user.state).press_tab()
        browser.element('[id="city"]').click()
        browser.element(f'[id="react-select-4-input"]').type(user.city).press_tab()


    def submit(self):
        browser.element('[id="submit"]').press_enter()

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

    # def check_filled_in_part_data(self, user_partly: User):
    #     browser.all('tbody tr').should(have.texts(f'Student Name' + ' ' + user_partly.name + ' ' + user_partly.surname,
    #                                                     f'Student Email' + ' ' + user_partly.email,
    #                                                     f'Gender' + ' ' + f'{user_partly.gender.value}',
    #                                                     f'Mobile' + ' ' + user_partly.mobile,
    #                                                     f'Date of Birth' + ' ' + f'{user_partly.date}' + ' ' + f'{user_partly.month}' + ',' + f'{user_partly.year}',
    #                                                     f'Subjects' + ' ' + user_partly.subject,
    #                                                     f'Hobbies' + ' ' + user_partly.hobbies,
    #                                                     f'Picture' + ' ' + user_partly.picture,
    #                                                     'Address' + ' ' + user_partly.address,
    #                                                     f'State and City' + ' ' + user_partly.state + ' ' + user_partly.city))
    #     return self

    def check_filled_in_part_data(self, user_partly: User):
        data = browser.all('tbody tr').texts(f'Student Name' + ' ' + user_partly.name + ' ' + user_partly.surname,
                                                        f'Student Email' + ' ' + user_partly.email,
                                                        f'Gender' + ' ' + f'{user_partly.gender.value}',
                                                        f'Mobile' + ' ' + user_partly.mobile,
                                                        f'Date of Birth' + ' ' + f'{user_partly.date}' + ' ' + f'{user_partly.month}' + ',' + f'{user_partly.year}',
                                                        f'Subjects' + ' ' + user_partly.subject,
                                                        f'Hobbies' + ' ' + user_partly.hobbies,
                                                        f'Picture' + ' ' + user_partly.picture,
                                                        'Address' + ' ' + user_partly.address,
                                                        f'State and City' + ' ' + user_partly.state + ' ' + user_partly.city)

        assert user_partly == data
        return self

