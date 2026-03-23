from setuptools import setup
setup(
    name='cli-anything-copy',
    version='1.0.0',
    packages=['cli_anything.copy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-copy=cli_anything.copy:cli']},
)
