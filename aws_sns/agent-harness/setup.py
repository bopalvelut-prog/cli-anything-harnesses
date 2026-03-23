from setuptools import setup
setup(
    name='cli-anything-aws_sns',
    version='1.0.0',
    packages=['cli_anything.aws_sns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_sns=cli_anything.aws_sns:cli']},
)
