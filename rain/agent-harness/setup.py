from setuptools import setup
setup(
    name='cli-anything-rain',
    version='1.0.0',
    packages=['cli_anything.rain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rain=cli_anything.rain:cli']},
)
