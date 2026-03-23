from setuptools import setup
setup(
    name='cli-anything-venture',
    version='1.0.0',
    packages=['cli_anything.venture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-venture=cli_anything.venture:cli']},
)
