from setuptools import setup
setup(
    name='cli-anything-saltstack',
    version='1.0.0',
    packages=['cli_anything.saltstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-saltstack=cli_anything.saltstack:cli']},
)
