from setuptools import setup
setup(
    name='cli-anything-nio',
    version='1.0.0',
    packages=['cli_anything.nio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nio=cli_anything.nio:cli']},
)
