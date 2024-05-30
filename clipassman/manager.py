# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from smartcliapp import Informer

from clipassman import __version__
from clipassman.commander import Commander


class CliMan(Informer):
    commander = Commander()
    name = 'clipassman'
    title = 'Cli Password Manager'
    description = 'Console Smart Password Generator and Manager'
    version = __version__
    copyright = 'Copyright © 2024, A.A. Suvorov'
    url = 'https://github.com/smartlegionlab/'
