from setuptools import setup
setup(
    name='cli-anything-idrive',
    version='1.0.0',
    packages=['cli_anything.idrive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-idrive=cli_anything.idrive:cli']},
)
