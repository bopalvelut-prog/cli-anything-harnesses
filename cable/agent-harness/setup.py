from setuptools import setup
setup(
    name='cli-anything-cable',
    version='1.0.0',
    packages=['cli_anything.cable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cable=cli_anything.cable:cli']},
)
