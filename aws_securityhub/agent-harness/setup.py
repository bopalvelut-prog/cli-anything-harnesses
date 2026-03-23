from setuptools import setup
setup(
    name='cli-anything-aws_securityhub',
    version='1.0.0',
    packages=['cli_anything.aws_securityhub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_securityhub=cli_anything.aws_securityhub:cli']},
)
