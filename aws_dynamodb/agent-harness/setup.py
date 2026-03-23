from setuptools import setup
setup(
    name='cli-anything-aws_dynamodb',
    version='1.0.0',
    packages=['cli_anything.aws_dynamodb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_dynamodb=cli_anything.aws_dynamodb:cli']},
)
