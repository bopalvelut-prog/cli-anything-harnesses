from setuptools import setup
setup(
    name='cli-anything-bfg',
    version='1.0.0',
    packages=['cli_anything.bfg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bfg=cli_anything.bfg:cli']},
)
