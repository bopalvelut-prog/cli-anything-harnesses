from setuptools import setup
setup(
    name='cli-anything-mux',
    version='1.0.0',
    packages=['cli_anything.mux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mux=cli_anything.mux:cli']},
)
