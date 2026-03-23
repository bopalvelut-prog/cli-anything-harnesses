from setuptools import setup
setup(
    name='cli-anything-aws_elasticbeanstalk',
    version='1.0.0',
    packages=['cli_anything.aws_elasticbeanstalk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_elasticbeanstalk=cli_anything.aws_elasticbeanstalk:cli']},
)
