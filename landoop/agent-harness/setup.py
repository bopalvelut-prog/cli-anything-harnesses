from setuptools import setup
setup(
    name='cli-anything-landoop',
    version='1.0.0',
    packages=['cli_anything.landoop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-landoop=cli_anything.landoop:cli']},
)
