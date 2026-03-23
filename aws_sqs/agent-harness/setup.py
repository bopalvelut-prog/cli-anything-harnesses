from setuptools import setup
setup(
    name='cli-anything-aws_sqs',
    version='1.0.0',
    packages=['cli_anything.aws_sqs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_sqs=cli_anything.aws_sqs:cli']},
)
