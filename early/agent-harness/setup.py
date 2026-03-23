from setuptools import setup
setup(
    name='cli-anything-early',
    version='1.0.0',
    packages=['cli_anything.early'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-early=cli_anything.early:cli']},
)
