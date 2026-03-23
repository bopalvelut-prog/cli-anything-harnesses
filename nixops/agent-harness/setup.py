from setuptools import setup
setup(
    name='cli-anything-nixops',
    version='1.0.0',
    packages=['cli_anything.nixops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nixops=cli_anything.nixops:cli']},
)
