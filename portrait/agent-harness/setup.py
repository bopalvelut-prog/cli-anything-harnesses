from setuptools import setup
setup(
    name='cli-anything-portrait',
    version='1.0.0',
    packages=['cli_anything.portrait'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-portrait=cli_anything.portrait:cli']},
)
