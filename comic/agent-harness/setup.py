from setuptools import setup
setup(
    name='cli-anything-comic',
    version='1.0.0',
    packages=['cli_anything.comic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-comic=cli_anything.comic:cli']},
)
