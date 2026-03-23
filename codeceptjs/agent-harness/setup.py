from setuptools import setup
setup(
    name='cli-anything-codeceptjs',
    version='1.0.0',
    packages=['cli_anything.codeceptjs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codeceptjs=cli_anything.codeceptjs:cli']},
)
