from setuptools import setup
setup(
    name='cli-anything-such',
    version='1.0.0',
    packages=['cli_anything.such'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-such=cli_anything.such:cli']},
)
