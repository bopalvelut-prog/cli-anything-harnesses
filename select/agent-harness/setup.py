from setuptools import setup
setup(
    name='cli-anything-select',
    version='1.0.0',
    packages=['cli_anything.select'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-select=cli_anything.select:cli']},
)
