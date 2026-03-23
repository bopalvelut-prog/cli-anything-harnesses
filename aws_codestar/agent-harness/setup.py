from setuptools import setup
setup(
    name='cli-anything-aws_codestar',
    version='1.0.0',
    packages=['cli_anything.aws_codestar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_codestar=cli_anything.aws_codestar:cli']},
)
