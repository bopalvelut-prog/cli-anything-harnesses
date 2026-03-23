from setuptools import setup
setup(
    name='cli-anything-jail',
    version='1.0.0',
    packages=['cli_anything.jail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jail=cli_anything.jail:cli']},
)
