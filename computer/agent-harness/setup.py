from setuptools import setup
setup(
    name='cli-anything-computer',
    version='1.0.0',
    packages=['cli_anything.computer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-computer=cli_anything.computer:cli']},
)
