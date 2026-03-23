from setuptools import setup
setup(
    name='cli-anything-codeigniter',
    version='1.0.0',
    packages=['cli_anything.codeigniter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codeigniter=cli_anything.codeigniter:cli']},
)
