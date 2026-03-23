from setuptools import setup
setup(
    name='cli-anything-last',
    version='1.0.0',
    packages=['cli_anything.last'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-last=cli_anything.last:cli']},
)
