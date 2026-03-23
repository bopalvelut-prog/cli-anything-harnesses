from setuptools import setup
setup(
    name='cli-anything-bank',
    version='1.0.0',
    packages=['cli_anything.bank'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bank=cli_anything.bank:cli']},
)
