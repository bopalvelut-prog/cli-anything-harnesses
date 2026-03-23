from setuptools import setup
setup(
    name='cli-anything-aws_lookout',
    version='1.0.0',
    packages=['cli_anything.aws_lookout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_lookout=cli_anything.aws_lookout:cli']},
)
