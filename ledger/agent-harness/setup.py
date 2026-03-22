from setuptools import setup
setup(
    name='cli-anything-ledger',
    version='1.0.0',
    packages=['cli_anything.ledger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ledger=cli_anything.ledger:cli']},
)
