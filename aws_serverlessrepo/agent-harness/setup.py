from setuptools import setup
setup(
    name='cli-anything-aws_serverlessrepo',
    version='1.0.0',
    packages=['cli_anything.aws_serverlessrepo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_serverlessrepo=cli_anything.aws_serverlessrepo:cli']},
)
