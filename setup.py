from setuptools import setup

setup(
    name='mydocgenerator',
    version='1.0',
    packages=['mydocgenerator'],
    entry_points={
        'console_scripts': [
            'mydocgenerator = mydocgenerator.mydocgenerator:main'
        ]
    }
)
