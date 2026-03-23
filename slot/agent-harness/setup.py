from setuptools import setup
setup(
    name='cli-anything-slot',
    version='1.0.0',
    packages=['cli_anything.slot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slot=cli_anything.slot:cli']},
)
