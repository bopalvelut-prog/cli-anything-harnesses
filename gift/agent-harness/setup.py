from setuptools import setup
setup(
    name='cli-anything-gift',
    version='1.0.0',
    packages=['cli_anything.gift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gift=cli_anything.gift:cli']},
)
