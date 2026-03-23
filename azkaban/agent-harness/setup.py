from setuptools import setup
setup(
    name='cli-anything-azkaban',
    version='1.0.0',
    packages=['cli_anything.azkaban'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azkaban=cli_anything.azkaban:cli']},
)
