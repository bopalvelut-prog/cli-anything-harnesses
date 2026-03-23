from setuptools import setup
setup(
    name='cli-anything-aws_vpc',
    version='1.0.0',
    packages=['cli_anything.aws_vpc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_vpc=cli_anything.aws_vpc:cli']},
)
