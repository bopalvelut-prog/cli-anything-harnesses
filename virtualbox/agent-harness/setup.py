from setuptools import setup
setup(
    name='cli-anything-virtualbox',
    version='1.0.0',
    packages=['cli_anything.virtualbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-virtualbox=cli_anything.virtualbox:cli']},
)
