from setuptools import setup
setup(
    name='cli-anything-tinyproxy',
    version='1.0.0',
    packages=['cli_anything.tinyproxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tinyproxy=cli_anything.tinyproxy:cli']},
)
