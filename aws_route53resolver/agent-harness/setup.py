from setuptools import setup
setup(
    name='cli-anything-aws_route53resolver',
    version='1.0.0',
    packages=['cli_anything.aws_route53resolver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_route53resolver=cli_anything.aws_route53resolver:cli']},
)
