from setuptools import setup
setup(
    name='cli-anything-rudder',
    version='1.0.0',
    packages=['cli_anything.rudder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rudder=cli_anything.rudder:cli']},
)
