from setuptools import setup
setup(
    name='cli-anything-scaling',
    version='1.0.0',
    packages=['cli_anything.scaling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scaling=cli_anything.scaling:cli']},
)
