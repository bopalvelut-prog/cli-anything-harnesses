from setuptools import setup
setup(
    name='cli-anything-aws_sqs_v4',
    version='1.0.0',
    packages=['cli_anything.aws_sqs_v4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_sqs_v4=cli_anything.aws_sqs_v4:cli']},
)
