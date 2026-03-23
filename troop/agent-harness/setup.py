from setuptools import setup
setup(
    name='cli-anything-troop',
    version='1.0.0',
    packages=['cli_anything.troop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-troop=cli_anything.troop:cli']},
)
