from setuptools import setup
setup(
    name='cli-anything-lunch',
    version='1.0.0',
    packages=['cli_anything.lunch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lunch=cli_anything.lunch:cli']},
)
