from setuptools import setup
setup(
    name='cli-anything-second',
    version='1.0.0',
    packages=['cli_anything.second'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-second=cli_anything.second:cli']},
)
