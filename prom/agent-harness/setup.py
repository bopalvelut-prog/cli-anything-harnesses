from setuptools import setup
setup(
    name='cli-anything-prom',
    version='1.0.0',
    packages=['cli_anything.prom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prom=cli_anything.prom:cli']},
)
