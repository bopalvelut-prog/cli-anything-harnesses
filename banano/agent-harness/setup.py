from setuptools import setup
setup(
    name='cli-anything-banano',
    version='1.0.0',
    packages=['cli_anything.banano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-banano=cli_anything.banano:cli']},
)
