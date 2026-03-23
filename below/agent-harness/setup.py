from setuptools import setup
setup(
    name='cli-anything-below',
    version='1.0.0',
    packages=['cli_anything.below'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-below=cli_anything.below:cli']},
)
