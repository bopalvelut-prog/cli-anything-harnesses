from setuptools import setup
setup(
    name='cli-anything-bend',
    version='1.0.0',
    packages=['cli_anything.bend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bend=cli_anything.bend:cli']},
)
