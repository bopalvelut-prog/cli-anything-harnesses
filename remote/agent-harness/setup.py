from setuptools import setup
setup(
    name='cli-anything-remote',
    version='1.0.0',
    packages=['cli_anything.remote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remote=cli_anything.remote:cli']},
)
