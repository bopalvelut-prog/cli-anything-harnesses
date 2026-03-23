from setuptools import setup
setup(
    name='cli-anything-rs',
    version='1.0.0',
    packages=['cli_anything.rs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rs=cli_anything.rs:cli']},
)
