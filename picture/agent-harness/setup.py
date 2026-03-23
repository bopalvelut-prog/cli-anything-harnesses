from setuptools import setup
setup(
    name='cli-anything-picture',
    version='1.0.0',
    packages=['cli_anything.picture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-picture=cli_anything.picture:cli']},
)
