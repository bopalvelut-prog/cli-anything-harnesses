from setuptools import setup
setup(
    name='cli-anything-weapon',
    version='1.0.0',
    packages=['cli_anything.weapon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weapon=cli_anything.weapon:cli']},
)
