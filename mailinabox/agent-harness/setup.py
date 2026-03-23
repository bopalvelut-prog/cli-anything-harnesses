from setuptools import setup
setup(
    name='cli-anything-mailinabox',
    version='1.0.0',
    packages=['cli_anything.mailinabox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mailinabox=cli_anything.mailinabox:cli']},
)
