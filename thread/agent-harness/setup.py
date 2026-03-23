from setuptools import setup
setup(
    name='cli-anything-thread',
    version='1.0.0',
    packages=['cli_anything.thread'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thread=cli_anything.thread:cli']},
)
