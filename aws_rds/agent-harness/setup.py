from setuptools import setup
setup(
    name='cli-anything-aws_rds',
    version='1.0.0',
    packages=['cli_anything.aws_rds'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_rds=cli_anything.aws_rds:cli']},
)
