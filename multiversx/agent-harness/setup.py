from setuptools import setup
setup(
    name='cli-anything-multiversx',
    version='1.0.0',
    packages=['cli_anything.multiversx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-multiversx=cli_anything.multiversx:cli']},
)
