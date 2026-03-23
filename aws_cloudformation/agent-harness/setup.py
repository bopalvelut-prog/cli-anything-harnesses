from setuptools import setup
setup(
    name='cli-anything-aws_cloudformation',
    version='1.0.0',
    packages=['cli_anything.aws_cloudformation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloudformation=cli_anything.aws_cloudformation:cli']},
)
