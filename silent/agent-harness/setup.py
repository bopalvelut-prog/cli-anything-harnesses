from setuptools import setup
setup(
    name='cli-anything-silent',
    version='1.0.0',
    packages=['cli_anything.silent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-silent=cli_anything.silent:cli']},
)
