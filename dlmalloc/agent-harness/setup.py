from setuptools import setup
setup(
    name='cli-anything-dlmalloc',
    version='1.0.0',
    packages=['cli_anything.dlmalloc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dlmalloc=cli_anything.dlmalloc:cli']},
)
