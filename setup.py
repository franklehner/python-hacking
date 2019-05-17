"""
setup.py
"""


from setuptools import setup, find_packages


setup(
    name="python-hacking",
    version="0.0.1",
    author="Frank Lehner",
    author_email="frank-lehner71@t-online.de",
    packages=find_packages(),
    install_requires=[
        "click",
        "attr",
        "sqlalchemy",
        "psycopg2",
    ],
    test_requires=[
        "pytest",
    ],
)
