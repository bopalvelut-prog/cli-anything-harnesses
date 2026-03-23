from setuptools import setup
setup(
    name='cli-anything-toy',
    version='1.0.0',
    packages=['cli_anything.toy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toy=cli_anything.toy:cli']},
)
