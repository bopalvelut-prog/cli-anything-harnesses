from setuptools import setup
setup(
    name='cli-anything-aws_signer',
    version='1.0.0',
    packages=['cli_anything.aws_signer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_signer=cli_anything.aws_signer:cli']},
)
