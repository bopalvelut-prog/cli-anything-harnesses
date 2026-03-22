from setuptools import setup
setup(
    name='cli-anything-chef',
    version='1.0.0',
    packages=['cli_anything.chef'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chef=cli_anything.chef:cli']},
)
