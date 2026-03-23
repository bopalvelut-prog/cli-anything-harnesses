from setuptools import setup
setup(
    name='cli-anything-favorite',
    version='1.0.0',
    packages=['cli_anything.favorite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-favorite=cli_anything.favorite:cli']},
)
