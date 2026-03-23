from setuptools import setup
setup(
    name='cli-anything-lb',
    version='1.0.0',
    packages=['cli_anything.lb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lb=cli_anything.lb:cli']},
)
