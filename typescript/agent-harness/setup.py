from setuptools import setup
setup(
    name='cli-anything-typescript',
    version='1.0.0',
    packages=['cli_anything.typescript'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-typescript=cli_anything.typescript:cli']},
)
