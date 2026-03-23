from setuptools import setup
setup(
    name='cli-anything-license',
    version='1.0.0',
    packages=['cli_anything.license'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-license=cli_anything.license:cli']},
)
