from setuptools import setup
setup(
    name='cli-anything-router',
    version='1.0.0',
    packages=['cli_anything.router'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-router=cli_anything.router:cli']},
)
