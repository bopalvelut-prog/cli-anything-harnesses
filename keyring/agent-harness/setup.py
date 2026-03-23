from setuptools import setup
setup(
    name='cli-anything-keyring',
    version='1.0.0',
    packages=['cli_anything.keyring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keyring=cli_anything.keyring:cli']},
)
