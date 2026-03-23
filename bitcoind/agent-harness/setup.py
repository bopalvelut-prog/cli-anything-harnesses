from setuptools import setup
setup(
    name='cli-anything-bitcoind',
    version='1.0.0',
    packages=['cli_anything.bitcoind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitcoind=cli_anything.bitcoind:cli']},
)
