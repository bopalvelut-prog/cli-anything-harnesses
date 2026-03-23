from setuptools import setup
setup(
    name='cli-anything-immutant',
    version='1.0.0',
    packages=['cli_anything.immutant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-immutant=cli_anything.immutant:cli']},
)
