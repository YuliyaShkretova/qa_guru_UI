from HW_5_5.registration import Registration


def test_form_fill_in(browser_setup):
    registration_form = Registration()
    registration_form.open()
    registration_form.fill_in_name('Юлия')
    registration_form.fill_in_surname('Шкретова')
    registration_form.fill_in_email('y.shk@mail.ru')
    registration_form.choose_gender('2')
    registration_form.fill_in_phone('1234567890')
    registration_form.fill_in_birthday('1990', 'November', '13')
    registration_form.fill_in_int('d', '0')
    registration_form.choose_hobbies('3')
    registration_form.load_image('sticker.jpg')
    registration_form.fill_in_address('Мурталь, Австрия')
    registration_form.choose_address('1', '0')
    registration_form.submit()
    registration_form.assert_user_data('Student Name Юлия Шкретова',
                                       'Student Email y.shk@mail.ru',
                                       'Gender Female',
                                       'Mobile 1234567890',
                                       'Date of Birth 13 November,1990',
                                       'Subjects Hindi',
                                       'Hobbies Music',
                                       'Picture sticker.jpg',
                                       'Address Мурталь, Австрия',
                                       'State and City Uttar Pradesh Agra')

