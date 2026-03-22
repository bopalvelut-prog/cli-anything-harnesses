from setuptools import setup
setup(
    name='cli-anything-formstack',
    version='1.0.0',
    packages=['cli_anything.formstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formstack=cli_anything.formstack:cli']},
)
