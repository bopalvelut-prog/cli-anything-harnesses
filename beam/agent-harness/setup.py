from setuptools import setup
setup(
    name='cli-anything-beam',
    version='1.0.0',
    packages=['cli_anything.beam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beam=cli_anything.beam:cli']},
)
