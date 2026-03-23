from setuptools import setup
setup(
    name='cli-anything-transaction',
    version='1.0.0',
    packages=['cli_anything.transaction'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-transaction=cli_anything.transaction:cli']},
)
