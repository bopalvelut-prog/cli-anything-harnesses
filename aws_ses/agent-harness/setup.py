from setuptools import setup
setup(
    name='cli-anything-aws_ses',
    version='1.0.0',
    packages=['cli_anything.aws_ses'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ses=cli_anything.aws_ses:cli']},
)
