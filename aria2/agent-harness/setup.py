from setuptools import setup
setup(
    name='cli-anything-aria2',
    version='1.0.0',
    packages=['cli_anything.aria2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aria2=cli_anything.aria2:cli']},
)
