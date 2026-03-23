from setuptools import setup
setup(
    name='cli-anything-finger',
    version='1.0.0',
    packages=['cli_anything.finger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-finger=cli_anything.finger:cli']},
)
