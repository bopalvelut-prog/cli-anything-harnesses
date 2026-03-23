from setuptools import setup
setup(
    name='cli-anything-format',
    version='1.0.0',
    packages=['cli_anything.format'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-format=cli_anything.format:cli']},
)
