from setuptools import setup
setup(
    name='cli-anything-aider',
    version='1.0.0',
    packages=['cli_anything.aider'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aider=cli_anything.aider:cli']},
)
