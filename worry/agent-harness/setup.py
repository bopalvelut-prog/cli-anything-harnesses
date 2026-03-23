from setuptools import setup
setup(
    name='cli-anything-worry',
    version='1.0.0',
    packages=['cli_anything.worry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worry=cli_anything.worry:cli']},
)
