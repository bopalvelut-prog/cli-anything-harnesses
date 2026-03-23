from setuptools import setup
setup(
    name='cli-anything-symmetry',
    version='1.0.0',
    packages=['cli_anything.symmetry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-symmetry=cli_anything.symmetry:cli']},
)
