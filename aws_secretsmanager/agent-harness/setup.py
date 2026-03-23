from setuptools import setup
setup(
    name='cli-anything-aws_secretsmanager',
    version='1.0.0',
    packages=['cli_anything.aws_secretsmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_secretsmanager=cli_anything.aws_secretsmanager:cli']},
)
