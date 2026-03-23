from setuptools import setup
setup(
    name='cli-anything-aws_batch',
    version='1.0.0',
    packages=['cli_anything.aws_batch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_batch=cli_anything.aws_batch:cli']},
)
