from setuptools import setup
setup(
    name='cli-anything-settle',
    version='1.0.0',
    packages=['cli_anything.settle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-settle=cli_anything.settle:cli']},
)
