from setuptools import setup
setup(
    name='cli-anything-stage',
    version='1.0.0',
    packages=['cli_anything.stage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stage=cli_anything.stage:cli']},
)
