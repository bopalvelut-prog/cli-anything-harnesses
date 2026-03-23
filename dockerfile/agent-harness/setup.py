from setuptools import setup
setup(
    name='cli-anything-dockerfile',
    version='1.0.0',
    packages=['cli_anything.dockerfile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dockerfile=cli_anything.dockerfile:cli']},
)
