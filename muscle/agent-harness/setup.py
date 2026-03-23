from setuptools import setup
setup(
    name='cli-anything-muscle',
    version='1.0.0',
    packages=['cli_anything.muscle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-muscle=cli_anything.muscle:cli']},
)
