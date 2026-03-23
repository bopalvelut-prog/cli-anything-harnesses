from setuptools import setup
setup(
    name='cli-anything-leader',
    version='1.0.0',
    packages=['cli_anything.leader'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leader=cli_anything.leader:cli']},
)
