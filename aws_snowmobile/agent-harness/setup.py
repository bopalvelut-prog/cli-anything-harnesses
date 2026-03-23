from setuptools import setup
setup(
    name='cli-anything-aws_snowmobile',
    version='1.0.0',
    packages=['cli_anything.aws_snowmobile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_snowmobile=cli_anything.aws_snowmobile:cli']},
)
