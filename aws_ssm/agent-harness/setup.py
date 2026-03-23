from setuptools import setup
setup(
    name='cli-anything-aws_ssm',
    version='1.0.0',
    packages=['cli_anything.aws_ssm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ssm=cli_anything.aws_ssm:cli']},
)
