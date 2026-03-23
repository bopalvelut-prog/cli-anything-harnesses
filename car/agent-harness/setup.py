from setuptools import setup
setup(
    name='cli-anything-car',
    version='1.0.0',
    packages=['cli_anything.car'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-car=cli_anything.car:cli']},
)
