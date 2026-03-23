from setuptools import setup
setup(
    name='cli-anything-aws_support',
    version='1.0.0',
    packages=['cli_anything.aws_support'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_support=cli_anything.aws_support:cli']},
)
