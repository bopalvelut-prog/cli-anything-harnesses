from setuptools import setup
setup(
    name='cli-anything-aws_codepipeline',
    version='1.0.0',
    packages=['cli_anything.aws_codepipeline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_codepipeline=cli_anything.aws_codepipeline:cli']},
)
