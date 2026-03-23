from setuptools import setup
setup(
    name='cli-anything-pretty',
    version='1.0.0',
    packages=['cli_anything.pretty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pretty=cli_anything.pretty:cli']},
)
