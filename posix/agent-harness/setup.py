from setuptools import setup
setup(
    name='cli-anything-posix',
    version='1.0.0',
    packages=['cli_anything.posix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-posix=cli_anything.posix:cli']},
)
