from setuptools import setup
setup(
    name='cli-anything-entry',
    version='1.0.0',
    packages=['cli_anything.entry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-entry=cli_anything.entry:cli']},
)
