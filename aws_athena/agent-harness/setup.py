from setuptools import setup
setup(
    name='cli-anything-aws_athena',
    version='1.0.0',
    packages=['cli_anything.aws_athena'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_athena=cli_anything.aws_athena:cli']},
)
