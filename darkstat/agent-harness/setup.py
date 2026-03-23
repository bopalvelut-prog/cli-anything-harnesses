from setuptools import setup
setup(
    name='cli-anything-darkstat',
    version='1.0.0',
    packages=['cli_anything.darkstat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-darkstat=cli_anything.darkstat:cli']},
)
