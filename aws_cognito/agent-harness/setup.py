from setuptools import setup
setup(
    name='cli-anything-aws_cognito',
    version='1.0.0',
    packages=['cli_anything.aws_cognito'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cognito=cli_anything.aws_cognito:cli']},
)
