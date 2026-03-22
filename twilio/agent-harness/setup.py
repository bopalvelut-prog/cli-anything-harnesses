from setuptools import setup
setup(
    name='cli-anything-twilio',
    version='1.0.0',
    packages=['cli_anything.twilio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twilio=cli_anything.twilio:cli']},
)
