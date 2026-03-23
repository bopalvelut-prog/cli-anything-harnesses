from setuptools import setup
setup(
    name='cli-anything-laboratory',
    version='1.0.0',
    packages=['cli_anything.laboratory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-laboratory=cli_anything.laboratory:cli']},
)
