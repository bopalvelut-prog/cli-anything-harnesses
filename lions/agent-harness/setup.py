from setuptools import setup
setup(
    name='cli-anything-lions',
    version='1.0.0',
    packages=['cli_anything.lions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lions=cli_anything.lions:cli']},
)
