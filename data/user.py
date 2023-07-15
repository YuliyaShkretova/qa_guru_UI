from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Subject(Enum):
    arts = 'Arts'
    maths = 'Maths'
    biology = 'Biology'


@dataclass
class User:

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
    subject=[Subject.maths],
    hobbies=[Hobbies.music],
    picture='sticker.jpg',
    address='Мурталь, Австрия',
    state='NCR',
    city='Delhi')
