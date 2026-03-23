from setuptools import setup
setup(
    name='cli-anything-verdaccio',
    version='1.0.0',
    packages=['cli_anything.verdaccio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-verdaccio=cli_anything.verdaccio:cli']},
)
