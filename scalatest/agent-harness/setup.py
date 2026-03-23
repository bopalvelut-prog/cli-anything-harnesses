from setuptools import setup
setup(
    name='cli-anything-scalatest',
    version='1.0.0',
    packages=['cli_anything.scalatest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scalatest=cli_anything.scalatest:cli']},
)
