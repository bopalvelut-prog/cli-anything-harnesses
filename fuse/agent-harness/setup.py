from setuptools import setup
setup(
    name='cli-anything-fuse',
    version='1.0.0',
    packages=['cli_anything.fuse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fuse=cli_anything.fuse:cli']},
)
