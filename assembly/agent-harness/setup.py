from setuptools import setup
setup(
    name='cli-anything-assembly',
    version='1.0.0',
    packages=['cli_anything.assembly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assembly=cli_anything.assembly:cli']},
)
