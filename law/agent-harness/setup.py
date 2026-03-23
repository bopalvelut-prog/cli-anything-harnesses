from setuptools import setup
setup(
    name='cli-anything-law',
    version='1.0.0',
    packages=['cli_anything.law'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-law=cli_anything.law:cli']},
)
