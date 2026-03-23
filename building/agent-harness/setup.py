from setuptools import setup
setup(
    name='cli-anything-building',
    version='1.0.0',
    packages=['cli_anything.building'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-building=cli_anything.building:cli']},
)
