from setuptools import setup
setup(
    name='cli-anything-rate',
    version='1.0.0',
    packages=['cli_anything.rate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rate=cli_anything.rate:cli']},
)
