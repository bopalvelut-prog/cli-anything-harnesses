from setuptools import setup
setup(
    name='cli-anything-memory',
    version='1.0.0',
    packages=['cli_anything.memory'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-memory=cli_anything.memory:cli']},
)
