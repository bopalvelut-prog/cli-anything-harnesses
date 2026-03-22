from setuptools import setup
setup(
    name='cli-anything-binance',
    version='1.0.0',
    packages=['cli_anything.binance'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-binance=cli_anything.binance:cli']},
)
