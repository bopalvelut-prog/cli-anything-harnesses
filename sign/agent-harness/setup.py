from setuptools import setup
setup(
    name='cli-anything-sign',
    version='1.0.0',
    packages=['cli_anything.sign'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sign=cli_anything.sign:cli']},
)
