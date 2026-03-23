from setuptools import setup
setup(
    name='cli-anything-rich',
    version='1.0.0',
    packages=['cli_anything.rich'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rich=cli_anything.rich:cli']},
)
