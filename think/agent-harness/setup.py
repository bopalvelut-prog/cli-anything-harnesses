from setuptools import setup
setup(
    name='cli-anything-think',
    version='1.0.0',
    packages=['cli_anything.think'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-think=cli_anything.think:cli']},
)
