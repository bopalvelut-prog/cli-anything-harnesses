from setuptools import setup
setup(
    name='cli-anything-aws_cloudfront',
    version='1.0.0',
    packages=['cli_anything.aws_cloudfront'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloudfront=cli_anything.aws_cloudfront:cli']},
)
