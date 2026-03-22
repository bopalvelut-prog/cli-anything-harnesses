from setuptools import setup
setup(
    name='cli-anything-sqlite',
    version='1.0.0',
    packages=['cli_anything.sqlite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sqlite=cli_anything.sqlite:cli']},
)
