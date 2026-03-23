from setuptools import setup
setup(
    name='cli-anything-chunk',
    version='1.0.0',
    packages=['cli_anything.chunk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chunk=cli_anything.chunk:cli']},
)
