from setuptools import setup
setup(
    name='cli-anything-eleventy',
    version='1.0.0',
    packages=['cli_anything.eleventy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eleventy=cli_anything.eleventy:cli']},
)
