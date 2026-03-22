from setuptools import setup
setup(
    name='cli-anything-remix',
    version='1.0.0',
    packages=['cli_anything.remix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remix=cli_anything.remix:cli']},
)
