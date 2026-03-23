from setuptools import setup
setup(
    name='cli-anything-file',
    version='1.0.0',
    packages=['cli_anything.file'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-file=cli_anything.file:cli']},
)
