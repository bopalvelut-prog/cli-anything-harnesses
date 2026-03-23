from setuptools import setup
setup(
    name='cli-anything-ring',
    version='1.0.0',
    packages=['cli_anything.ring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ring=cli_anything.ring:cli']},
)
