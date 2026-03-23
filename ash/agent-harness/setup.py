from setuptools import setup
setup(
    name='cli-anything-ash',
    version='1.0.0',
    packages=['cli_anything.ash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ash=cli_anything.ash:cli']},
)
