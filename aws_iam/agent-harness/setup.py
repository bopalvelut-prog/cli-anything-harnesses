from setuptools import setup
setup(
    name='cli-anything-aws_iam',
    version='1.0.0',
    packages=['cli_anything.aws_iam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_iam=cli_anything.aws_iam:cli']},
)
