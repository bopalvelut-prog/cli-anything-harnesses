from setuptools import setup
setup(
    name='cli-anything-society',
    version='1.0.0',
    packages=['cli_anything.society'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-society=cli_anything.society:cli']},
)
