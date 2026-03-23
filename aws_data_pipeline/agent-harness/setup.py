from setuptools import setup
setup(
    name='cli-anything-aws_data_pipeline',
    version='1.0.0',
    packages=['cli_anything.aws_data_pipeline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_data_pipeline=cli_anything.aws_data_pipeline:cli']},
)
