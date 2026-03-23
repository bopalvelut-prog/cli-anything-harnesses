from setuptools import setup
setup(
    name='cli-anything-fever',
    version='1.0.0',
    packages=['cli_anything.fever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fever=cli_anything.fever:cli']},
)
