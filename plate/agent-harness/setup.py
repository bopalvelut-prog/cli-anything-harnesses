from setuptools import setup
setup(
    name='cli-anything-plate',
    version='1.0.0',
    packages=['cli_anything.plate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plate=cli_anything.plate:cli']},
)
