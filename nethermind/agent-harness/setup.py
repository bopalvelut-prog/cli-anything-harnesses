from setuptools import setup
setup(
    name='cli-anything-nethermind',
    version='1.0.0',
    packages=['cli_anything.nethermind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nethermind=cli_anything.nethermind:cli']},
)
