# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import shutil


class OutputManager:

    @classmethod
    def print_text(cls, text='', symbol='-'):
        width = cls._get_term_width()
        text = f' {text} ' if text else ''
        print(text.center(width, symbol))

    @classmethod
    def _get_term_width(cls):
        return shutil.get_terminal_size()[0]
