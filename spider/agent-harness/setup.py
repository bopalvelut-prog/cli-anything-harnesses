from setuptools import setup
setup(
    name='cli-anything-spider',
    version='1.0.0',
    packages=['cli_anything.spider'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spider=cli_anything.spider:cli']},
)
