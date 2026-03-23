from setuptools import setup
setup(
    name='cli-anything-soil',
    version='1.0.0',
    packages=['cli_anything.soil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soil=cli_anything.soil:cli']},
)
