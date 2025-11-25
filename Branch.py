from Account import Account
from typing import List

class Branch:
    def __init__(self, number: str, name: str, location: str, phone: str):
        self._number = number
        self._name = name
        self._location = location
        self._phone = phone
        self._accounts: List['Account'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
        pass