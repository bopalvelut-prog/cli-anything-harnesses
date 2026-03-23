from setuptools import setup
setup(
    name='cli-anything-crisis',
    version='1.0.0',
    packages=['cli_anything.crisis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crisis=cli_anything.crisis:cli']},
)
