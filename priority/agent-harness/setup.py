from setuptools import setup
setup(
    name='cli-anything-priority',
    version='1.0.0',
    packages=['cli_anything.priority'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-priority=cli_anything.priority:cli']},
)
