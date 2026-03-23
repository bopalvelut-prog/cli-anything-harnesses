from setuptools import setup
setup(
    name='cli-anything-soccer',
    version='1.0.0',
    packages=['cli_anything.soccer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soccer=cli_anything.soccer:cli']},
)
