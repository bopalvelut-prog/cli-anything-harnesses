from setuptools import setup
setup(
    name='cli-anything-mikmod',
    version='1.0.0',
    packages=['cli_anything.mikmod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mikmod=cli_anything.mikmod:cli']},
)
