from setuptools import setup
setup(
    name='cli-anything-sacred',
    version='1.0.0',
    packages=['cli_anything.sacred'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sacred=cli_anything.sacred:cli']},
)
