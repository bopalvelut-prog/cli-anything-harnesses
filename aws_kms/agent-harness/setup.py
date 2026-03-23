from setuptools import setup
setup(
    name='cli-anything-aws_kms',
    version='1.0.0',
    packages=['cli_anything.aws_kms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_kms=cli_anything.aws_kms:cli']},
)
