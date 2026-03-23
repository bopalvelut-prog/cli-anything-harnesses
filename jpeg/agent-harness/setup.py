from setuptools import setup
setup(
    name='cli-anything-jpeg',
    version='1.0.0',
    packages=['cli_anything.jpeg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jpeg=cli_anything.jpeg:cli']},
)
