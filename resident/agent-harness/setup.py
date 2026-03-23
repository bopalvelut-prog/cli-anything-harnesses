from setuptools import setup
setup(
    name='cli-anything-resident',
    version='1.0.0',
    packages=['cli_anything.resident'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resident=cli_anything.resident:cli']},
)
