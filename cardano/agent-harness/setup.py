from setuptools import setup
setup(
    name='cli-anything-cardano',
    version='1.0.0',
    packages=['cli_anything.cardano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cardano=cli_anything.cardano:cli']},
)
