from setuptools import setup
setup(
    name='cli-anything-porter',
    version='1.0.0',
    packages=['cli_anything.porter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-porter=cli_anything.porter:cli']},
)
