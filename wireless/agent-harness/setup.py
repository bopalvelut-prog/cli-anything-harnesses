from setuptools import setup
setup(
    name='cli-anything-wireless',
    version='1.0.0',
    packages=['cli_anything.wireless'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wireless=cli_anything.wireless:cli']},
)
