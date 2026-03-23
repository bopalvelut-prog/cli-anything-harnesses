from setuptools import setup
setup(
    name='cli-anything-dspace',
    version='1.0.0',
    packages=['cli_anything.dspace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dspace=cli_anything.dspace:cli']},
)
