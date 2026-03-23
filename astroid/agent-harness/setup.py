from setuptools import setup
setup(
    name='cli-anything-astroid',
    version='1.0.0',
    packages=['cli_anything.astroid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-astroid=cli_anything.astroid:cli']},
)
