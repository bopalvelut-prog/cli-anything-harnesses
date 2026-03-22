from setuptools import setup
setup(
    name='cli-anything-telegraf',
    version='1.0.0',
    packages=['cli_anything.telegraf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-telegraf=cli_anything.telegraf:cli']},
)
