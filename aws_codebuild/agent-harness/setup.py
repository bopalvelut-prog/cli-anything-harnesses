from setuptools import setup
setup(
    name='cli-anything-aws_codebuild',
    version='1.0.0',
    packages=['cli_anything.aws_codebuild'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_codebuild=cli_anything.aws_codebuild:cli']},
)
