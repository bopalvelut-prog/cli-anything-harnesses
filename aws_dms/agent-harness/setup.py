from setuptools import setup
setup(
    name='cli-anything-aws_dms',
    version='1.0.0',
    packages=['cli_anything.aws_dms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_dms=cli_anything.aws_dms:cli']},
)
