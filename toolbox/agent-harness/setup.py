from setuptools import setup
setup(
    name='cli-anything-toolbox',
    version='1.0.0',
    packages=['cli_anything.toolbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toolbox=cli_anything.toolbox:cli']},
)
