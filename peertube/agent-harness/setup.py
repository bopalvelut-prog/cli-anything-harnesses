from setuptools import setup
setup(
    name='cli-anything-peertube',
    version='1.0.0',
    packages=['cli_anything.peertube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peertube=cli_anything.peertube:cli']},
)
