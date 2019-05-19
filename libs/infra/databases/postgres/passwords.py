"""
passwords.py
============
"""


import crypt as _crypt


class Password:
    """
    Password
    """

    @classmethod
    def encrypt(cls, password, salt):
        """
        encrypt
        """
        return _crypt.crypt(password, salt)

    @classmethod
    def check_password(cls, code, password, salt):
        """
        decrypt
        """
        return _crypt.crypt(password, salt) == code
