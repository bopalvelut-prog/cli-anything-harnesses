from setuptools import setup
setup(
    name='cli-anything-choir',
    version='1.0.0',
    packages=['cli_anything.choir'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-choir=cli_anything.choir:cli']},
)
