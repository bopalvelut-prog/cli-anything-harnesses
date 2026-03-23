from setuptools import setup
setup(
    name='cli-anything-gparted',
    version='1.0.0',
    packages=['cli_anything.gparted'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gparted=cli_anything.gparted:cli']},
)
