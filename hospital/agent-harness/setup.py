from setuptools import setup
setup(
    name='cli-anything-hospital',
    version='1.0.0',
    packages=['cli_anything.hospital'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hospital=cli_anything.hospital:cli']},
)
