from setuptools import setup
setup(
    name='cli-anything-stride',
    version='1.0.0',
    packages=['cli_anything.stride'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stride=cli_anything.stride:cli']},
)
