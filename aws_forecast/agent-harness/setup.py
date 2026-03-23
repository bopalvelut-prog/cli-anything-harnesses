from setuptools import setup
setup(
    name='cli-anything-aws_forecast',
    version='1.0.0',
    packages=['cli_anything.aws_forecast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_forecast=cli_anything.aws_forecast:cli']},
)
