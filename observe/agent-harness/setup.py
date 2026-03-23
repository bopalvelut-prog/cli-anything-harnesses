from setuptools import setup
setup(
    name='cli-anything-observe',
    version='1.0.0',
    packages=['cli_anything.observe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-observe=cli_anything.observe:cli']},
)
