from setuptools import setup
setup(
    name='cli-anything-terra',
    version='1.0.0',
    packages=['cli_anything.terra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terra=cli_anything.terra:cli']},
)
