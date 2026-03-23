from setuptools import setup
setup(
    name='cli-anything-datasets',
    version='1.0.0',
    packages=['cli_anything.datasets'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datasets=cli_anything.datasets:cli']},
)
