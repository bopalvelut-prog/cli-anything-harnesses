from setuptools import setup
setup(
    name='cli-anything-aws_networkmanager',
    version='1.0.0',
    packages=['cli_anything.aws_networkmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_networkmanager=cli_anything.aws_networkmanager:cli']},
)
