from setuptools import setup
setup(
    name='cli-anything-classic',
    version='1.0.0',
    packages=['cli_anything.classic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-classic=cli_anything.classic:cli']},
)
