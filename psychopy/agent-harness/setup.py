from setuptools import setup
setup(
    name='cli-anything-psychopy',
    version='1.0.0',
    packages=['cli_anything.psychopy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-psychopy=cli_anything.psychopy:cli']},
)
