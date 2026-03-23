from setuptools import setup
setup(
    name='cli-anything-address',
    version='1.0.0',
    packages=['cli_anything.address'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-address=cli_anything.address:cli']},
)
