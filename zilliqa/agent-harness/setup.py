from setuptools import setup
setup(
    name='cli-anything-zilliqa',
    version='1.0.0',
    packages=['cli_anything.zilliqa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zilliqa=cli_anything.zilliqa:cli']},
)
