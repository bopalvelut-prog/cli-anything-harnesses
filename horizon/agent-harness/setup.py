from setuptools import setup
setup(
    name='cli-anything-horizon',
    version='1.0.0',
    packages=['cli_anything.horizon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-horizon=cli_anything.horizon:cli']},
)
