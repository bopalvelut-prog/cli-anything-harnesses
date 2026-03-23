from setuptools import setup
setup(
    name='cli-anything-peloton',
    version='1.0.0',
    packages=['cli_anything.peloton'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-peloton=cli_anything.peloton:cli']},
)
