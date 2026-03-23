from setuptools import setup
setup(
    name='cli-anything-application',
    version='1.0.0',
    packages=['cli_anything.application'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-application=cli_anything.application:cli']},
)
