# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------


class SmartPassword:

    def __init__(self, login='', key='', length=12):
        self._login = login
        self._length = length
        self._key = key

    @property
    def login(self):
        return self._login

    @property
    def key(self):
        return self._key

    @property
    def length(self):
        return self._length


class SmartPasswordFactory:

    @classmethod
    def create_smart_password(cls, login, key, length):
        return SmartPassword(login=login, key=key, length=length)
