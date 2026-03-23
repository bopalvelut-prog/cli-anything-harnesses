from setuptools import setup
setup(
    name='cli-anything-gentle',
    version='1.0.0',
    packages=['cli_anything.gentle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gentle=cli_anything.gentle:cli']},
)
