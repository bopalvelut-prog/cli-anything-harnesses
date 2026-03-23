from setuptools import setup
setup(
    name='cli-anything-dcgm',
    version='1.0.0',
    packages=['cli_anything.dcgm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dcgm=cli_anything.dcgm:cli']},
)
