from setuptools import setup
setup(
    name='cli-anything-aws_appsync',
    version='1.0.0',
    packages=['cli_anything.aws_appsync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_appsync=cli_anything.aws_appsync:cli']},
)
