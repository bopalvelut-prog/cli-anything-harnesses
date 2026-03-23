from setuptools import setup
setup(
    name='cli-anything-aws_connect',
    version='1.0.0',
    packages=['cli_anything.aws_connect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_connect=cli_anything.aws_connect:cli']},
)
