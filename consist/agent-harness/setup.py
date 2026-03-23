from setuptools import setup
setup(
    name='cli-anything-consist',
    version='1.0.0',
    packages=['cli_anything.consist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-consist=cli_anything.consist:cli']},
)
