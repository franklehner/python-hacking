"""
encrypt_password_crpyt.py
=========================
"""

import sys as _sys
import getpass as _getpass


def get_password():
    """
    get password
    """
    password = _getpass.getpass("Bitte geben Sie das Passwort ein: ")
    if _getpass.getpass("Bitte wiederholen Sie das Passwort") == password:
        return password
    _sys.exit(1)


def generate_password(salt):
    """
    generate password
    """
    password = get_password()
    print(password, salt)
