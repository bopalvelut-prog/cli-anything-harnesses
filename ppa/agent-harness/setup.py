from setuptools import setup
setup(
    name='cli-anything-ppa',
    version='1.0.0',
    packages=['cli_anything.ppa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ppa=cli_anything.ppa:cli']},
)
