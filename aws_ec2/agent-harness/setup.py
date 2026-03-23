from setuptools import setup
setup(
    name='cli-anything-aws_ec2',
    version='1.0.0',
    packages=['cli_anything.aws_ec2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ec2=cli_anything.aws_ec2:cli']},
)
