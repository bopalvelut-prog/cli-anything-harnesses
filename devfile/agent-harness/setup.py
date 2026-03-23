from setuptools import setup
setup(
    name='cli-anything-devfile',
    version='1.0.0',
    packages=['cli_anything.devfile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-devfile=cli_anything.devfile:cli']},
)
