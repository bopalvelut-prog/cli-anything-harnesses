from setuptools import setup
setup(
    name='cli-anything-vast',
    version='1.0.0',
    packages=['cli_anything.vast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vast=cli_anything.vast:cli']},
)
