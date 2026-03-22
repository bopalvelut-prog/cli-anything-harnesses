from setuptools import setup
setup(
    name='cli-anything-moonriver',
    version='1.0.0',
    packages=['cli_anything.moonriver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moonriver=cli_anything.moonriver:cli']},
)
