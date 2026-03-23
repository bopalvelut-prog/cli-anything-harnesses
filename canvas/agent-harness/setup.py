from setuptools import setup
setup(
    name='cli-anything-canvas',
    version='1.0.0',
    packages=['cli_anything.canvas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-canvas=cli_anything.canvas:cli']},
)
