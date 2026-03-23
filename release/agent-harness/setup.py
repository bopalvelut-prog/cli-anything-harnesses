from setuptools import setup
setup(
    name='cli-anything-release',
    version='1.0.0',
    packages=['cli_anything.release'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-release=cli_anything.release:cli']},
)
