from setuptools import setup
setup(
    name='cli-anything-digibyte',
    version='1.0.0',
    packages=['cli_anything.digibyte'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-digibyte=cli_anything.digibyte:cli']},
)
