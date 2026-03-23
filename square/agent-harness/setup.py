from setuptools import setup
setup(
    name='cli-anything-square',
    version='1.0.0',
    packages=['cli_anything.square'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-square=cli_anything.square:cli']},
)
