from setuptools import setup
setup(
    name='cli-anything-mechanism',
    version='1.0.0',
    packages=['cli_anything.mechanism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mechanism=cli_anything.mechanism:cli']},
)
