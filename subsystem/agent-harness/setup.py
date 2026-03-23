from setuptools import setup
setup(
    name='cli-anything-subsystem',
    version='1.0.0',
    packages=['cli_anything.subsystem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subsystem=cli_anything.subsystem:cli']},
)
