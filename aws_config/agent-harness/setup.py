from setuptools import setup
setup(
    name='cli-anything-aws_config',
    version='1.0.0',
    packages=['cli_anything.aws_config'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_config=cli_anything.aws_config:cli']},
)
