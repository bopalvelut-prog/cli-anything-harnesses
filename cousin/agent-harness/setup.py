from setuptools import setup
setup(
    name='cli-anything-cousin',
    version='1.0.0',
    packages=['cli_anything.cousin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cousin=cli_anything.cousin:cli']},
)
