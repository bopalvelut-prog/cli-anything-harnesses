from setuptools import setup
setup(
    name='cli-anything-rest',
    version='1.0.0',
    packages=['cli_anything.rest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rest=cli_anything.rest:cli']},
)
