from setuptools import setup
setup(
    name='cli-anything-horror',
    version='1.0.0',
    packages=['cli_anything.horror'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-horror=cli_anything.horror:cli']},
)
