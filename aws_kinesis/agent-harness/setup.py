from setuptools import setup
setup(
    name='cli-anything-aws_kinesis',
    version='1.0.0',
    packages=['cli_anything.aws_kinesis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_kinesis=cli_anything.aws_kinesis:cli']},
)
