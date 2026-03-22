from setuptools import setup
setup(
    name='cli-anything-zeromq',
    version='1.0.0',
    packages=['cli_anything.zeromq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zeromq=cli_anything.zeromq:cli']},
)
