from setuptools import setup
setup(
    name='cli-anything-aws_savingsplans',
    version='1.0.0',
    packages=['cli_anything.aws_savingsplans'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_savingsplans=cli_anything.aws_savingsplans:cli']},
)
