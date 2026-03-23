from setuptools import setup
setup(
    name='cli-anything-environment',
    version='1.0.0',
    packages=['cli_anything.environment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-environment=cli_anything.environment:cli']},
)
