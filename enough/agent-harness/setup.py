from setuptools import setup
setup(
    name='cli-anything-enough',
    version='1.0.0',
    packages=['cli_anything.enough'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enough=cli_anything.enough:cli']},
)
