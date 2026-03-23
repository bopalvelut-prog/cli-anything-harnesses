from setuptools import setup
setup(
    name='cli-anything-fleet',
    version='1.0.0',
    packages=['cli_anything.fleet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fleet=cli_anything.fleet:cli']},
)
