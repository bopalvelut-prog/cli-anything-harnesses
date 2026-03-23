from setuptools import setup
setup(
    name='cli-anything-rubber',
    version='1.0.0',
    packages=['cli_anything.rubber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rubber=cli_anything.rubber:cli']},
)
