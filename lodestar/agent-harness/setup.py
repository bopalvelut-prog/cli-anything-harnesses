from setuptools import setup
setup(
    name='cli-anything-lodestar',
    version='1.0.0',
    packages=['cli_anything.lodestar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lodestar=cli_anything.lodestar:cli']},
)
