from setuptools import setup
setup(
    name='cli-anything-musical',
    version='1.0.0',
    packages=['cli_anything.musical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-musical=cli_anything.musical:cli']},
)
