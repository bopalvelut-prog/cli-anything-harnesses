from setuptools import setup
setup(
    name='cli-anything-dear',
    version='1.0.0',
    packages=['cli_anything.dear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dear=cli_anything.dear:cli']},
)
