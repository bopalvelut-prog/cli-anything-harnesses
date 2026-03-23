from setuptools import setup
setup(
    name='cli-anything-academy',
    version='1.0.0',
    packages=['cli_anything.academy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-academy=cli_anything.academy:cli']},
)
