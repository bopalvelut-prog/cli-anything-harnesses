from setuptools import setup
setup(
    name='cli-anything-runway',
    version='1.0.0',
    packages=['cli_anything.runway'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-runway=cli_anything.runway:cli']},
)
