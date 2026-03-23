from setuptools import setup
setup(
    name='cli-anything-aws_snowcone',
    version='1.0.0',
    packages=['cli_anything.aws_snowcone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_snowcone=cli_anything.aws_snowcone:cli']},
)
