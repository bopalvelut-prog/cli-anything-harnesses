from setuptools import setup
setup(
    name='cli-anything-guard',
    version='1.0.0',
    packages=['cli_anything.guard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guard=cli_anything.guard:cli']},
)
