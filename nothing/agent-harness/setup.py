from setuptools import setup
setup(
    name='cli-anything-nothing',
    version='1.0.0',
    packages=['cli_anything.nothing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nothing=cli_anything.nothing:cli']},
)
