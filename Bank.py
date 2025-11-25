from datetime import datetime
from typing import List
from abc import ABC, abstractmethod
from Branch import Branch



class Bank:
    def __init__(self, name: str, cnpj: str, location: str, phone: str):
        self._name = name
        self._cnpj = cnpj
        self._location = location
        self._phone = phone
        self._branch: List['Branch'] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        self._cnpj = value

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
        
    def add_branch(self, branch: 'Branch'):
        if isinstance(branch, Branch):
            self._branch.append(branch)
            print("Branch added successfully")
        else:
            raise ValueError("The following is not a branch") #fazer exception personalizada 
        
    def show_branches(self):
        for branch in self._branch:
            print(f"Branch: {branch.name}")
        else: 
            print("Branck vazia")