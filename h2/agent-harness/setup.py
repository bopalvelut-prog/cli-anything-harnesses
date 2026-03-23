from setuptools import setup
setup(
    name='cli-anything-h2',
    version='1.0.0',
    packages=['cli_anything.h2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-h2=cli_anything.h2:cli']},
)
