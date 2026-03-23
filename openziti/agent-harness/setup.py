from setuptools import setup
setup(
    name='cli-anything-openziti',
    version='1.0.0',
    packages=['cli_anything.openziti'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openziti=cli_anything.openziti:cli']},
)
