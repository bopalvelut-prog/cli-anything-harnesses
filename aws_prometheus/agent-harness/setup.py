from setuptools import setup
setup(
    name='cli-anything-aws_prometheus',
    version='1.0.0',
    packages=['cli_anything.aws_prometheus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_prometheus=cli_anything.aws_prometheus:cli']},
)
