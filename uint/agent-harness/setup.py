from setuptools import setup
setup(
    name='cli-anything-uint',
    version='1.0.0',
    packages=['cli_anything.uint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uint=cli_anything.uint:cli']},
)
