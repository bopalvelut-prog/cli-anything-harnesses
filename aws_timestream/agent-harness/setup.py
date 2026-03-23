from setuptools import setup
setup(
    name='cli-anything-aws_timestream',
    version='1.0.0',
    packages=['cli_anything.aws_timestream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_timestream=cli_anything.aws_timestream:cli']},
)
