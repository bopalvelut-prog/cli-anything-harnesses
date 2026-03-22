from setuptools import setup
setup(
    name='cli-anything-librephotos',
    version='1.0.0',
    packages=['cli_anything.librephotos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-librephotos=cli_anything.librephotos:cli']},
)
