# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 01:00:34 2021

@author: Notebook
"""
from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        print("All checks")

    @abstractmethod
    def land(self):
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        super().fly()
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")

jet1 = Jet()
jet1.land()
jet1.fly()
