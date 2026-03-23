from setuptools import setup
setup(
    name='cli-anything-scratch',
    version='1.0.0',
    packages=['cli_anything.scratch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scratch=cli_anything.scratch:cli']},
)
