from setuptools import setup
setup(
    name='cli-anything-amethyst',
    version='1.0.0',
    packages=['cli_anything.amethyst'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amethyst=cli_anything.amethyst:cli']},
)
