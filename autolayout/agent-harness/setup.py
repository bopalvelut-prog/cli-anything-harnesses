from setuptools import setup
setup(
    name='cli-anything-autolayout',
    version='1.0.0',
    packages=['cli_anything.autolayout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autolayout=cli_anything.autolayout:cli']},
)
