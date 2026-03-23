from setuptools import setup
setup(
    name='cli-anything-slice',
    version='1.0.0',
    packages=['cli_anything.slice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slice=cli_anything.slice:cli']},
)
