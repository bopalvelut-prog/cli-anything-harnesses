from setuptools import setup
setup(
    name='cli-anything-bitcoin',
    version='1.0.0',
    packages=['cli_anything.bitcoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitcoin=cli_anything.bitcoin:cli']},
)
