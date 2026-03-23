from setuptools import setup
setup(
    name='cli-anything-kitchen',
    version='1.0.0',
    packages=['cli_anything.kitchen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kitchen=cli_anything.kitchen:cli']},
)
