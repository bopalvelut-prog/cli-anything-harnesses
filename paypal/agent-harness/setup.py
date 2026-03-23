from setuptools import setup
setup(
    name='cli-anything-paypal',
    version='1.0.0',
    packages=['cli_anything.paypal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-paypal=cli_anything.paypal:cli']},
)
