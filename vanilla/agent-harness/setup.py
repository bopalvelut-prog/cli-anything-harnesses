from setuptools import setup
setup(
    name='cli-anything-vanilla',
    version='1.0.0',
    packages=['cli_anything.vanilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vanilla=cli_anything.vanilla:cli']},
)
