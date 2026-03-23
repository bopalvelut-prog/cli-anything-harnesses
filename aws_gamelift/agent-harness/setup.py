from setuptools import setup
setup(
    name='cli-anything-aws_gamelift',
    version='1.0.0',
    packages=['cli_anything.aws_gamelift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_gamelift=cli_anything.aws_gamelift:cli']},
)
