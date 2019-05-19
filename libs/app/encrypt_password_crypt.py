"""
encrypt_password_crpyt.py
=========================
"""

import sys as _sys
import getpass as _getpass

import libs.domain.usecases.encrypt_password_crypt as _usecase


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
    encrypter = _usecase.Encrypter(password, salt)
    encrypted = encrypter.generate_password()
    print(encrypted)
