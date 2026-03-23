from setuptools import setup
setup(
    name='cli-anything-hvac',
    version='1.0.0',
    packages=['cli_anything.hvac'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hvac=cli_anything.hvac:cli']},
)
