from setuptools import setup
setup(
    name='cli-anything-aws_trusted_advisor',
    version='1.0.0',
    packages=['cli_anything.aws_trusted_advisor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_trusted_advisor=cli_anything.aws_trusted_advisor:cli']},
)
