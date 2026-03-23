from setuptools import setup
setup(
    name='cli-anything-drawing',
    version='1.0.0',
    packages=['cli_anything.drawing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drawing=cli_anything.drawing:cli']},
)
