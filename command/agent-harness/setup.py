from setuptools import setup
setup(
    name='cli-anything-command',
    version='1.0.0',
    packages=['cli_anything.command'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-command=cli_anything.command:cli']},
)
