from setuptools import setup
setup(
    name='cli-anything-country',
    version='1.0.0',
    packages=['cli_anything.country'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-country=cli_anything.country:cli']},
)
