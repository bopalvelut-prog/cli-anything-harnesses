from setuptools import setup
setup(
    name='cli-anything-variable',
    version='1.0.0',
    packages=['cli_anything.variable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-variable=cli_anything.variable:cli']},
)
