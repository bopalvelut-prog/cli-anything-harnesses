from setuptools import setup
setup(
    name='cli-anything-barn',
    version='1.0.0',
    packages=['cli_anything.barn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-barn=cli_anything.barn:cli']},
)
