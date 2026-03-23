from setuptools import setup
setup(
    name='cli-anything-pdb',
    version='1.0.0',
    packages=['cli_anything.pdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pdb=cli_anything.pdb:cli']},
)
