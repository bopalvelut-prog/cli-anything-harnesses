from setuptools import setup
setup(
    name='cli-anything-install',
    version='1.0.0',
    packages=['cli_anything.install'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-install=cli_anything.install:cli']},
)
