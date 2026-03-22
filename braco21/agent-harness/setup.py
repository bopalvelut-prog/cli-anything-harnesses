from setuptools import setup
setup(
    name='cli-anything-braco21',
    version='1.0.0',
    packages=['cli_anything.braco21'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco21=cli_anything.braco21:cli']},
)
