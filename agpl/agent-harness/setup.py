from setuptools import setup
setup(
    name='cli-anything-agpl',
    version='1.0.0',
    packages=['cli_anything.agpl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agpl=cli_anything.agpl:cli']},
)
