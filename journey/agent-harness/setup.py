from setuptools import setup
setup(
    name='cli-anything-journey',
    version='1.0.0',
    packages=['cli_anything.journey'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-journey=cli_anything.journey:cli']},
)
