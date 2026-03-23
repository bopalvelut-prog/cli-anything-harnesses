from setuptools import setup
setup(
    name='cli-anything-aws_location',
    version='1.0.0',
    packages=['cli_anything.aws_location'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_location=cli_anything.aws_location:cli']},
)
