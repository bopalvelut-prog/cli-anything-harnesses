from setuptools import setup
setup(
    name='cli-anything-data',
    version='1.0.0',
    packages=['cli_anything.data'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-data=cli_anything.data:cli']},
)
