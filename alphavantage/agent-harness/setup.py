from setuptools import setup
setup(
    name='cli-anything-alphavantage',
    version='1.0.0',
    packages=['cli_anything.alphavantage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alphavantage=cli_anything.alphavantage:cli']},
)
