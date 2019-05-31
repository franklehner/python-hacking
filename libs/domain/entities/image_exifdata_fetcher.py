"""
imagage_exifdata_fetcher.py
"""


import abc as _abc


class ExifData(_abc.ABCMeta):
    """
    ExifDataClass
    """
    @_abc.abstractmethod
    def load(cls, path):
        """
        load
        """
        raise NotImplementedError

    @_abc.abstractmethod
    def read(cls, path):
        """
        read
        """
        raise NotImplementedError

    @_abc.abstractmethod
    def get(cls, data):
        """
        get
        """
        raise NotImplementedError
