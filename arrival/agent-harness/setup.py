from setuptools import setup
setup(
    name='cli-anything-arrival',
    version='1.0.0',
    packages=['cli_anything.arrival'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arrival=cli_anything.arrival:cli']},
)
