from setuptools import setup
setup(
    name='cli-anything-ciao',
    version='1.0.0',
    packages=['cli_anything.ciao'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ciao=cli_anything.ciao:cli']},
)
