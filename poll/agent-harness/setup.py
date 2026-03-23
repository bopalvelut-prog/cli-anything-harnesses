from setuptools import setup
setup(
    name='cli-anything-poll',
    version='1.0.0',
    packages=['cli_anything.poll'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poll=cli_anything.poll:cli']},
)
