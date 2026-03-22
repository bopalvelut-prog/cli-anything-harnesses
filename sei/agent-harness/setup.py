from setuptools import setup
setup(
    name='cli-anything-sei',
    version='1.0.0',
    packages=['cli_anything.sei'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sei=cli_anything.sei:cli']},
)
