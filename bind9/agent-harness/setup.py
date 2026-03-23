from setuptools import setup
setup(
    name='cli-anything-bind9',
    version='1.0.0',
    packages=['cli_anything.bind9'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bind9=cli_anything.bind9:cli']},
)
