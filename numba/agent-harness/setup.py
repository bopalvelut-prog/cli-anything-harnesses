from setuptools import setup
setup(
    name='cli-anything-numba',
    version='1.0.0',
    packages=['cli_anything.numba'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-numba=cli_anything.numba:cli']},
)
