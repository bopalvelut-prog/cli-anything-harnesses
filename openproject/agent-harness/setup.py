from setuptools import setup
setup(
    name='cli-anything-openproject',
    version='1.0.0',
    packages=['cli_anything.openproject'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openproject=cli_anything.openproject:cli']},
)
