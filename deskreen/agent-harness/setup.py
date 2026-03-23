from setuptools import setup
setup(
    name='cli-anything-deskreen',
    version='1.0.0',
    packages=['cli_anything.deskreen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deskreen=cli_anything.deskreen:cli']},
)
