from setuptools import setup
setup(
    name='cli-anything-aws_datasync',
    version='1.0.0',
    packages=['cli_anything.aws_datasync'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_datasync=cli_anything.aws_datasync:cli']},
)
