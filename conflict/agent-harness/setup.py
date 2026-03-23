from setuptools import setup
setup(
    name='cli-anything-conflict',
    version='1.0.0',
    packages=['cli_anything.conflict'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conflict=cli_anything.conflict:cli']},
)
