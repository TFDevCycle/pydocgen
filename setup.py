from setuptools import setup

setup(
    name='mydocgenerator',
    version='1.0',
    packages=['mydocgenerator'],
    long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
    entry_points={
        'console_scripts': [
            'mydocgenerator = mydocgenerator.mydocgenerator:main'
        ]
    }
)
