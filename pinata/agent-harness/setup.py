from setuptools import setup
setup(
    name='cli-anything-pinata',
    version='1.0.0',
    packages=['cli_anything.pinata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pinata=cli_anything.pinata:cli']},
)
