from setuptools import setup
setup(
    name='cli-anything-civil',
    version='1.0.0',
    packages=['cli_anything.civil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-civil=cli_anything.civil:cli']},
)
