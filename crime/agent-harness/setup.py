from setuptools import setup
setup(
    name='cli-anything-crime',
    version='1.0.0',
    packages=['cli_anything.crime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crime=cli_anything.crime:cli']},
)
