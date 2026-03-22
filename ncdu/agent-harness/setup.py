from setuptools import setup
setup(
    name='cli-anything-ncdu',
    version='1.0.0',
    packages=['cli_anything.ncdu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ncdu=cli_anything.ncdu:cli']},
)
