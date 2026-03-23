from setuptools import setup
setup(
    name='cli-anything-clipper',
    version='1.0.0',
    packages=['cli_anything.clipper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clipper=cli_anything.clipper:cli']},
)
