from importlib.metadata import entry_points
from setuptools import setup
from setuptools import find_packages

setup(
    name='MotiYoda',
    version='1.0.0',
    description='This package contains MotiYoda program for sending/emailing personalized motivational messages',
    author='Grace Ohlsen and Max Meiser',
    author_email='grace.ohlsen@colorado.edu',
    url='https://github.com/maxwmeiser/hackathon-march2022',
    packages=find_packages(),
    install_requires=[
        'smtplib',
        'email.message',
        'validate_email_address',
        're',
        'requests',
        'email',
        'json'
    ]
    entry_points={
        'console_scripts': [
            'moti-yoda-cli = app.py.main:main'
        ]
    }
)