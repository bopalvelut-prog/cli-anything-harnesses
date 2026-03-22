from setuptools import setup
setup(
    name='cli-anything-phantom',
    version='1.0.0',
    packages=['cli_anything.phantom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phantom=cli_anything.phantom:cli']},
)
