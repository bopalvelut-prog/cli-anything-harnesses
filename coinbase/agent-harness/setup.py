from setuptools import setup
setup(
    name='cli-anything-coinbase',
    version='1.0.0',
    packages=['cli_anything.coinbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coinbase=cli_anything.coinbase:cli']},
)
