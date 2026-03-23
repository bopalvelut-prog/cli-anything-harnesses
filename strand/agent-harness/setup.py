from setuptools import setup
setup(
    name='cli-anything-strand',
    version='1.0.0',
    packages=['cli_anything.strand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strand=cli_anything.strand:cli']},
)
