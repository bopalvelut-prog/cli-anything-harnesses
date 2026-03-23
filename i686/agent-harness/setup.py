from setuptools import setup
setup(
    name='cli-anything-i686',
    version='1.0.0',
    packages=['cli_anything.i686'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-i686=cli_anything.i686:cli']},
)
