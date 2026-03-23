from setuptools import setup
setup(
    name='cli-anything-large',
    version='1.0.0',
    packages=['cli_anything.large'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-large=cli_anything.large:cli']},
)
