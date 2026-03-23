from setuptools import setup
setup(
    name='cli-anything-bitcoin_core',
    version='1.0.0',
    packages=['cli_anything.bitcoin_core'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitcoin_core=cli_anything.bitcoin_core:cli']},
)
