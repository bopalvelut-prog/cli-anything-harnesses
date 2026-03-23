from setuptools import setup
setup(
    name='cli-anything-aws_codecommit',
    version='1.0.0',
    packages=['cli_anything.aws_codecommit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_codecommit=cli_anything.aws_codecommit:cli']},
)
