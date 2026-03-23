from setuptools import setup
setup(
    name='cli-anything-doozer',
    version='1.0.0',
    packages=['cli_anything.doozer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-doozer=cli_anything.doozer:cli']},
)
