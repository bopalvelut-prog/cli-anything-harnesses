from setuptools import setup
setup(
    name='cli-anything-aws_cdk',
    version='1.0.0',
    packages=['cli_anything.aws_cdk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cdk=cli_anything.aws_cdk:cli']},
)
