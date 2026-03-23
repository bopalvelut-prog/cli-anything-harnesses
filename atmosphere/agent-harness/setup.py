from setuptools import setup
setup(
    name='cli-anything-atmosphere',
    version='1.0.0',
    packages=['cli_anything.atmosphere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atmosphere=cli_anything.atmosphere:cli']},
)
