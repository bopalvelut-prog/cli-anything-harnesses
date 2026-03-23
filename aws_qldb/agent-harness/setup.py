from setuptools import setup
setup(
    name='cli-anything-aws_qldb',
    version='1.0.0',
    packages=['cli_anything.aws_qldb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_qldb=cli_anything.aws_qldb:cli']},
)
