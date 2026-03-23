from setuptools import setup
setup(
    name='cli-anything-famous',
    version='1.0.0',
    packages=['cli_anything.famous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-famous=cli_anything.famous:cli']},
)
