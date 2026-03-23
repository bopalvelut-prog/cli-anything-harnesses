from setuptools import setup
setup(
    name='cli-anything-metal',
    version='1.0.0',
    packages=['cli_anything.metal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metal=cli_anything.metal:cli']},
)
