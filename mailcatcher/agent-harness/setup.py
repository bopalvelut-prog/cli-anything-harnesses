from setuptools import setup
setup(
    name='cli-anything-mailcatcher',
    version='1.0.0',
    packages=['cli_anything.mailcatcher'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailcatcher=cli_anything.mailcatcher:cli']},
)
