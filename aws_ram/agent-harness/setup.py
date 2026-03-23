from setuptools import setup
setup(
    name='cli-anything-aws_ram',
    version='1.0.0',
    packages=['cli_anything.aws_ram'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ram=cli_anything.aws_ram:cli']},
)
