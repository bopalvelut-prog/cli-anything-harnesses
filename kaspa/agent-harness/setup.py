from setuptools import setup
setup(
    name='cli-anything-kaspa',
    version='1.0.0',
    packages=['cli_anything.kaspa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kaspa=cli_anything.kaspa:cli']},
)
