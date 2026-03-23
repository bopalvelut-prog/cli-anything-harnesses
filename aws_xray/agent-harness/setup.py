from setuptools import setup
setup(
    name='cli-anything-aws_xray',
    version='1.0.0',
    packages=['cli_anything.aws_xray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_xray=cli_anything.aws_xray:cli']},
)
