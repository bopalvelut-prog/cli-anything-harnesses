from setuptools import setup
setup(
    name='cli-anything-h2o',
    version='1.0.0',
    packages=['cli_anything.h2o'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-h2o=cli_anything.h2o:cli']},
)
