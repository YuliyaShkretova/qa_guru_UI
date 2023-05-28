from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

#
# class Subject(Enum):
#     hindi = 'Hindi'
#     social_studies = 'Social Studies'


@dataclass
class User:
    # name: str
    # surname: str
    # email: str
    # gender: Gender
    # mobile: str
    # date_of_birth: date
    # subject: List[Subject]
    # hobbies: List[Hobbies]
    # picture: str
    # address: str
    # state: str
    # city: str

    def __init__(self, name, surname, email, gender, mobile, year, month, date, subject, hobbies, picture, address,
                 state,
                 city):
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.year = year
        self.month = month
        self.date = date
        self.subject = subject
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city


user = User(
    name='Юлия',
    surname='Шкретова',
    email='y.shk@mail.ru',
    gender=Gender.female,
    mobile='1234567890',
    year=1991,
    month='October',
    date=13,
    subject='Hindi',
    hobbies='Music',
    picture='sticker.jpg',
    address='Мурталь, Австрия',
    state='NCR',
    city='Noida')
