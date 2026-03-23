from setuptools import setup
setup(
    name='cli-anything-vertical',
    version='1.0.0',
    packages=['cli_anything.vertical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vertical=cli_anything.vertical:cli']},
)
