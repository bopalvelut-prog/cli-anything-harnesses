from setuptools import setup
setup(
    name='cli-anything-aws_license',
    version='1.0.0',
    packages=['cli_anything.aws_license'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_license=cli_anything.aws_license:cli']},
)
