from setuptools import setup
setup(
    name='cli-anything-hg',
    version='1.0.0',
    packages=['cli_anything.hg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hg=cli_anything.hg:cli']},
)
