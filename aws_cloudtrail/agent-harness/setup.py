from setuptools import setup
setup(
    name='cli-anything-aws_cloudtrail',
    version='1.0.0',
    packages=['cli_anything.aws_cloudtrail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloudtrail=cli_anything.aws_cloudtrail:cli']},
)
