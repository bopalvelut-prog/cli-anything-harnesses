from setuptools import setup
setup(
    name='cli-anything-cython',
    version='1.0.0',
    packages=['cli_anything.cython'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cython=cli_anything.cython:cli']},
)
