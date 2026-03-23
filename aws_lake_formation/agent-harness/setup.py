from setuptools import setup
setup(
    name='cli-anything-aws_lake_formation',
    version='1.0.0',
    packages=['cli_anything.aws_lake_formation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_lake_formation=cli_anything.aws_lake_formation:cli']},
)
