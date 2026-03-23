from setuptools import setup
setup(
    name='cli-anything-aspen',
    version='1.0.0',
    packages=['cli_anything.aspen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aspen=cli_anything.aspen:cli']},
)
