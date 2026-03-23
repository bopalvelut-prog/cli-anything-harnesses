from setuptools import setup
setup(
    name='cli-anything-aws_glue',
    version='1.0.0',
    packages=['cli_anything.aws_glue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_glue=cli_anything.aws_glue:cli']},
)
