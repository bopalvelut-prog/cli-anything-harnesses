from setuptools import setup
setup(
    name='cli-anything-sas',
    version='1.0.0',
    packages=['cli_anything.sas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sas=cli_anything.sas:cli']},
)
