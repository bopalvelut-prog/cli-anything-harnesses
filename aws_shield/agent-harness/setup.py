from setuptools import setup
setup(
    name='cli-anything-aws_shield',
    version='1.0.0',
    packages=['cli_anything.aws_shield'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_shield=cli_anything.aws_shield:cli']},
)
