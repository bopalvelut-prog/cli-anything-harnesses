from setuptools import setup
setup(
    name='cli-anything-ticket',
    version='1.0.0',
    packages=['cli_anything.ticket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ticket=cli_anything.ticket:cli']},
)
