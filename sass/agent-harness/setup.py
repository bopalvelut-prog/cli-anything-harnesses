from setuptools import setup
setup(
    name='cli-anything-sass',
    version='1.0.0',
    packages=['cli_anything.sass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sass=cli_anything.sass:cli']},
)
