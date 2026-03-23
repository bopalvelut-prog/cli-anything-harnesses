from setuptools import setup
setup(
    name='cli-anything-aqueduct',
    version='1.0.0',
    packages=['cli_anything.aqueduct'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aqueduct=cli_anything.aqueduct:cli']},
)
