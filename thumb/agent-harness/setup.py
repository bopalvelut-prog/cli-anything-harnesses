from setuptools import setup
setup(
    name='cli-anything-thumb',
    version='1.0.0',
    packages=['cli_anything.thumb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thumb=cli_anything.thumb:cli']},
)
