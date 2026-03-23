from setuptools import setup
setup(
    name='cli-anything-aws_docdb',
    version='1.0.0',
    packages=['cli_anything.aws_docdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_docdb=cli_anything.aws_docdb:cli']},
)
