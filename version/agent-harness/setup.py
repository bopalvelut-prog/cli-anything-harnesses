from setuptools import setup
setup(
    name='cli-anything-version',
    version='1.0.0',
    packages=['cli_anything.version'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-version=cli_anything.version:cli']},
)
