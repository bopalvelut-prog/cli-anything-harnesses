from setuptools import setup
setup(
    name='cli-anything-aws_lambda',
    version='1.0.0',
    packages=['cli_anything.aws_lambda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_lambda=cli_anything.aws_lambda:cli']},
)
