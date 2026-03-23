from setuptools import setup
setup(
    name='cli-anything-apple_pay',
    version='1.0.0',
    packages=['cli_anything.apple_pay'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apple_pay=cli_anything.apple_pay:cli']},
)
