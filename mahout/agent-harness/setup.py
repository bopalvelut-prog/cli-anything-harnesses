from setuptools import setup
setup(
    name='cli-anything-mahout',
    version='1.0.0',
    packages=['cli_anything.mahout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mahout=cli_anything.mahout:cli']},
)
