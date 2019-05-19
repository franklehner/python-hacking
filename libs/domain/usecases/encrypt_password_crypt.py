"""
encrypt_password_crypt.py
=========================
"""


import attr as _attr

import libs.infra.databases.postgres.passwords as _infra


@_attr.s
class Encrypter:
    """
    Encrypter
    """

    password = _attr.ib()
    salt = _attr.ib()

    def encrypt(self):
        """
        encrypt
        """
        return _infra.Password.encrypt(self.password, self.salt)

    def generate_password(self):
        """
        generate_password
        """
        return self.encrypt()
