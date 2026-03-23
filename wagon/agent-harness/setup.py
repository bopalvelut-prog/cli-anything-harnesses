from setuptools import setup
setup(
    name='cli-anything-wagon',
    version='1.0.0',
    packages=['cli_anything.wagon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wagon=cli_anything.wagon:cli']},
)
