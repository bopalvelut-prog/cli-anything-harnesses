from setuptools import setup
setup(
    name='cli-anything-buildpack',
    version='1.0.0',
    packages=['cli_anything.buildpack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buildpack=cli_anything.buildpack:cli']},
)
