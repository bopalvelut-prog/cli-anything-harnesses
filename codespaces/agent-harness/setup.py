from setuptools import setup
setup(
    name='cli-anything-codespaces',
    version='1.0.0',
    packages=['cli_anything.codespaces'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codespaces=cli_anything.codespaces:cli']},
)
