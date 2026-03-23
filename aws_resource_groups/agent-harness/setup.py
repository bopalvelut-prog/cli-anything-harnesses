from setuptools import setup
setup(
    name='cli-anything-aws_resource_groups',
    version='1.0.0',
    packages=['cli_anything.aws_resource_groups'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_resource_groups=cli_anything.aws_resource_groups:cli']},
)
