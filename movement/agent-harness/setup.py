from setuptools import setup
setup(
    name='cli-anything-movement',
    version='1.0.0',
    packages=['cli_anything.movement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-movement=cli_anything.movement:cli']},
)
