from setuptools import setup
setup(
    name='cli-anything-webpack',
    version='1.0.0',
    packages=['cli_anything.webpack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-webpack=cli_anything.webpack:cli']},
)
