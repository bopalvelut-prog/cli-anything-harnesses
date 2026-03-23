from setuptools import setup
setup(
    name='cli-anything-phase',
    version='1.0.0',
    packages=['cli_anything.phase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phase=cli_anything.phase:cli']},
)
