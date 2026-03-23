from setuptools import setup
setup(
    name='cli-anything-urge',
    version='1.0.0',
    packages=['cli_anything.urge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-urge=cli_anything.urge:cli']},
)
