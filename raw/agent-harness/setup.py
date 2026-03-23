from setuptools import setup
setup(
    name='cli-anything-raw',
    version='1.0.0',
    packages=['cli_anything.raw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raw=cli_anything.raw:cli']},
)
