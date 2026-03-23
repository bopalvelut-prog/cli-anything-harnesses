from setuptools import setup
setup(
    name='cli-anything-moreover',
    version='1.0.0',
    packages=['cli_anything.moreover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moreover=cli_anything.moreover:cli']},
)
