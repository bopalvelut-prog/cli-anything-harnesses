from setuptools import setup
setup(
    name='cli-anything-superrare',
    version='1.0.0',
    packages=['cli_anything.superrare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-superrare=cli_anything.superrare:cli']},
)
