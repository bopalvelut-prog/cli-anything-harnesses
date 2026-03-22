from setuptools import setup
setup(
    name='cli-anything-temporal',
    version='1.0.0',
    packages=['cli_anything.temporal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-temporal=cli_anything.temporal:cli']},
)
