# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import click

from clipassman.manager import CliMan


@click.group(
    context_settings={'help_option_names': ['-h', '--help']},
    invoke_without_command=True
)
@click.version_option(f'{CliMan.name} v{CliMan.version}')
def cli():
    CliMan.show_head()
    CliMan.commander.run()
    CliMan.show_footer()


if __name__ == '__main__':
    cli()
