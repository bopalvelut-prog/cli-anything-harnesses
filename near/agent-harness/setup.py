from setuptools import setup
setup(
    name='cli-anything-near',
    version='1.0.0',
    packages=['cli_anything.near'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-near=cli_anything.near:cli']},
)
