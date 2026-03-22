from setuptools import setup
setup(
    name='cli-anything-braco44',
    version='1.0.0',
    packages=['cli_anything.braco44'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco44=cli_anything.braco44:cli']},
)
