from setuptools import setup
setup(
    name='cli-anything-prepare',
    version='1.0.0',
    packages=['cli_anything.prepare'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prepare=cli_anything.prepare:cli']},
)
