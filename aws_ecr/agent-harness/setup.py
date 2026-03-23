from setuptools import setup
setup(
    name='cli-anything-aws_ecr',
    version='1.0.0',
    packages=['cli_anything.aws_ecr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ecr=cli_anything.aws_ecr:cli']},
)
