from setuptools import setup
setup(
    name='cli-anything-cache',
    version='1.0.0',
    packages=['cli_anything.cache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cache=cli_anything.cache:cli']},
)
