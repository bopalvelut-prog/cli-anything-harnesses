from setuptools import setup
setup(
    name='cli-anything-airtable',
    version='1.0.0',
    packages=['cli_anything.airtable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-airtable=cli_anything.airtable:cli']},
)
