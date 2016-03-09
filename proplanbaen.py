#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'


class ProplanBean :
    msex = -1
    mage = -1
    myears = 0
    mbaoe = -1
    mbaof = -1
    duration = -1

    # def __init__(self, sex, age,years,baoe,baof):
    #     self.msex = sex
    #     self.mage = age
    #     self.myears = years
    #     self.mbaoe = baoe
    #     self.mbaof = baof

    def __init__(self, sex, age,years,baoe,baof,duration):
        self.msex = sex
        self.mage = age
        self.myears = years
        self.mbaoe = baoe
        self.mbaof = baof
        self.duration = duration


