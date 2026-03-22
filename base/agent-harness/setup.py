from setuptools import setup
setup(
    name='cli-anything-base',
    version='1.0.0',
    packages=['cli_anything.base'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-base=cli_anything.base:cli']},
)
