from setuptools import setup
setup(
    name='cli-anything-typeahead',
    version='1.0.0',
    packages=['cli_anything.typeahead'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typeahead=cli_anything.typeahead:cli']},
)
