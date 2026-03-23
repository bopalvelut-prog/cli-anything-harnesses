from setuptools import setup
setup(
    name='cli-anything-aws_comprehend',
    version='1.0.0',
    packages=['cli_anything.aws_comprehend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_comprehend=cli_anything.aws_comprehend:cli']},
)
