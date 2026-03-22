from setuptools import setup
setup(
    name='cli-anything-decred',
    version='1.0.0',
    packages=['cli_anything.decred'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decred=cli_anything.decred:cli']},
)
