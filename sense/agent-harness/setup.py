from setuptools import setup
setup(
    name='cli-anything-sense',
    version='1.0.0',
    packages=['cli_anything.sense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sense=cli_anything.sense:cli']},
)
