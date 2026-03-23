from setuptools import setup
setup(
    name='cli-anything-aws_stepfunctions',
    version='1.0.0',
    packages=['cli_anything.aws_stepfunctions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_stepfunctions=cli_anything.aws_stepfunctions:cli']},
)
