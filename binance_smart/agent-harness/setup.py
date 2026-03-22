from setuptools import setup
setup(
    name='cli-anything-binance_smart',
    version='1.0.0',
    packages=['cli_anything.binance_smart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-binance_smart=cli_anything.binance_smart:cli']},
)
