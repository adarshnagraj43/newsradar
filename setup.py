from setuptools import setup

setup(
    name='NewsRadar',
    version='1.0.0',
    packages=['app'],
    install_requires=[
        'Flask',
        'requests'
    ],
)