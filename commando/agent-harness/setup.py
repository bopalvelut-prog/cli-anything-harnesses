from setuptools import setup
setup(
    name='cli-anything-commando',
    version='1.0.0',
    packages=['cli_anything.commando'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-commando=cli_anything.commando:cli']},
)
