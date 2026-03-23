from setuptools import setup
setup(
    name='cli-anything-ping',
    version='1.0.0',
    packages=['cli_anything.ping'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ping=cli_anything.ping:cli']},
)
