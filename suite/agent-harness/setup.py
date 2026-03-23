from setuptools import setup
setup(
    name='cli-anything-suite',
    version='1.0.0',
    packages=['cli_anything.suite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suite=cli_anything.suite:cli']},
)
