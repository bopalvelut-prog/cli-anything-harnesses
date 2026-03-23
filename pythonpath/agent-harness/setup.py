from setuptools import setup
setup(
    name='cli-anything-pythonpath',
    version='1.0.0',
    packages=['cli_anything.pythonpath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pythonpath=cli_anything.pythonpath:cli']},
)
