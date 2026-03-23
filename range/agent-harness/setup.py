from setuptools import setup
setup(
    name='cli-anything-range',
    version='1.0.0',
    packages=['cli_anything.range'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-range=cli_anything.range:cli']},
)
