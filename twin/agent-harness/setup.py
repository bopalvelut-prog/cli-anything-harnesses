from setuptools import setup
setup(
    name='cli-anything-twin',
    version='1.0.0',
    packages=['cli_anything.twin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twin=cli_anything.twin:cli']},
)
