from setuptools import setup
setup(
    name='cli-anything-chrony',
    version='1.0.0',
    packages=['cli_anything.chrony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chrony=cli_anything.chrony:cli']},
)
