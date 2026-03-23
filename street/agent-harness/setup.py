from setuptools import setup
setup(
    name='cli-anything-street',
    version='1.0.0',
    packages=['cli_anything.street'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-street=cli_anything.street:cli']},
)
