import os

from selene.support.shared import browser
from selene import be, have, command, by


def test_form_fill_in(browser_setup):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type('Юлия')
    browser.element('[id="lastName"]').should(be.blank).type('Шкретова')
    browser.element('[id="userEmail"]').should(be.blank).type('y.shk@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option:nth-child(91)').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="10"]').click()
    browser.element('.react-datepicker__day--013').click()
    browser.element('[id="subjectsInput"]').should(be.blank).type('d')
    browser.element('[id=react-select-2-option-0]').double_click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd() + '/sticker.jpg')
    browser.element('[id="currentAddress"]').should(be.blank).type('Мурталь, Австрия')
    browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-1"]').should(have.text('Uttar Pradesh')).click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-0"]').should(have.text('Agra')).click()
    browser.element('[id="submit"]').perform(command.js.scroll_into_view)
    browser.element('[id="submit"]').press_enter()

    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(
        have.exact_texts('Юлия Шкретова', 'y.shk@mail.ru', 'Female', '1234567890', '13 November,1990', 'Hindi', 'Music',
                         'sticker.jpg', 'Мурталь, Австрия', 'Uttar Pradesh Agra'))
