from setuptools import setup
setup(
    name='cli-anything-aws_data_exchange',
    version='1.0.0',
    packages=['cli_anything.aws_data_exchange'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_data_exchange=cli_anything.aws_data_exchange:cli']},
)
