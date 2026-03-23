from setuptools import setup
setup(
    name='cli-anything-separate',
    version='1.0.0',
    packages=['cli_anything.separate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-separate=cli_anything.separate:cli']},
)
