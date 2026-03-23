from setuptools import setup
setup(
    name='cli-anything-sq',
    version='1.0.0',
    packages=['cli_anything.sq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sq=cli_anything.sq:cli']},
)
