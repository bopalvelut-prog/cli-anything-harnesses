from setuptools import setup
setup(
    name='cli-anything-slave',
    version='1.0.0',
    packages=['cli_anything.slave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slave=cli_anything.slave:cli']},
)
