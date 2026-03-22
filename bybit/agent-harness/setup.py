from setuptools import setup
setup(
    name='cli-anything-bybit',
    version='1.0.0',
    packages=['cli_anything.bybit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bybit=cli_anything.bybit:cli']},
)
