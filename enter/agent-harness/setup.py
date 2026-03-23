from setuptools import setup
setup(
    name='cli-anything-enter',
    version='1.0.0',
    packages=['cli_anything.enter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enter=cli_anything.enter:cli']},
)
