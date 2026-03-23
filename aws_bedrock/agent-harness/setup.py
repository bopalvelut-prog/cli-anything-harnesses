from setuptools import setup
setup(
    name='cli-anything-aws_bedrock',
    version='1.0.0',
    packages=['cli_anything.aws_bedrock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_bedrock=cli_anything.aws_bedrock:cli']},
)
