from setuptools import setup
setup(
    name='cli-anything-crash',
    version='1.0.0',
    packages=['cli_anything.crash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crash=cli_anything.crash:cli']},
)
