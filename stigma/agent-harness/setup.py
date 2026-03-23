from setuptools import setup
setup(
    name='cli-anything-stigma',
    version='1.0.0',
    packages=['cli_anything.stigma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stigma=cli_anything.stigma:cli']},
)
