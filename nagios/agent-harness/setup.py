from setuptools import setup
setup(
    name='cli-anything-nagios',
    version='1.0.0',
    packages=['cli_anything.nagios'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nagios=cli_anything.nagios:cli']},
)
