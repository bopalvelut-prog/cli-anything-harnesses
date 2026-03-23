from setuptools import setup
setup(
    name='cli-anything-occupy',
    version='1.0.0',
    packages=['cli_anything.occupy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-occupy=cli_anything.occupy:cli']},
)
