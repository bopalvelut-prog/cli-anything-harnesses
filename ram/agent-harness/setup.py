from setuptools import setup
setup(
    name='cli-anything-ram',
    version='1.0.0',
    packages=['cli_anything.ram'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ram=cli_anything.ram:cli']},
)
