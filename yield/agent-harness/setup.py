from setuptools import setup
setup(
    name='cli-anything-yield',
    version='1.0.0',
    packages=['cli_anything.yield'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yield=cli_anything.yield:cli']},
)
