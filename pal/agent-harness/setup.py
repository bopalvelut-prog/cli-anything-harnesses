from setuptools import setup
setup(
    name='cli-anything-pal',
    version='1.0.0',
    packages=['cli_anything.pal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pal=cli_anything.pal:cli']},
)
