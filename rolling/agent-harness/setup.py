from setuptools import setup
setup(
    name='cli-anything-rolling',
    version='1.0.0',
    packages=['cli_anything.rolling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rolling=cli_anything.rolling:cli']},
)
