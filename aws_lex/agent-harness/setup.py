from setuptools import setup
setup(
    name='cli-anything-aws_lex',
    version='1.0.0',
    packages=['cli_anything.aws_lex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_lex=cli_anything.aws_lex:cli']},
)
