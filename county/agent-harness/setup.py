from setuptools import setup
setup(
    name='cli-anything-county',
    version='1.0.0',
    packages=['cli_anything.county'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-county=cli_anything.county:cli']},
)
