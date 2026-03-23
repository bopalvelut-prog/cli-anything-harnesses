from setuptools import setup
setup(
    name='cli-anything-aws_cli',
    version='1.0.0',
    packages=['cli_anything.aws_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cli=cli_anything.aws_cli:cli']},
)
