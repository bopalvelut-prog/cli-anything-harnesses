from setuptools import setup
setup(
    name='cli-anything-aws_pinpoint',
    version='1.0.0',
    packages=['cli_anything.aws_pinpoint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_pinpoint=cli_anything.aws_pinpoint:cli']},
)
