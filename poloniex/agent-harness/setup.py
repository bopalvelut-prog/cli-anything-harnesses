from setuptools import setup
setup(
    name='cli-anything-poloniex',
    version='1.0.0',
    packages=['cli_anything.poloniex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poloniex=cli_anything.poloniex:cli']},
)
