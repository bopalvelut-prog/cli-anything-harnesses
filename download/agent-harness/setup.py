from setuptools import setup
setup(
    name='cli-anything-download',
    version='1.0.0',
    packages=['cli_anything.download'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-download=cli_anything.download:cli']},
)
