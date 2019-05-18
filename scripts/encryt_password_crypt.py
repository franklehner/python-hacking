"""
encrypt_password_crpyt.py
=========================
"""


import click as _click

import libs.app.encrypt_password_crypt as _app


@_click.command()
@_click.option("--salt", default="HX")
def cli(salt):
    """
    Client
    """
    _app.generate_password(salt)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
