from setuptools import setup
setup(
    name='cli-anything-aws_cloudmap',
    version='1.0.0',
    packages=['cli_anything.aws_cloudmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_cloudmap=cli_anything.aws_cloudmap:cli']},
)
