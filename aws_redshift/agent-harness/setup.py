from setuptools import setup
setup(
    name='cli-anything-aws_redshift',
    version='1.0.0',
    packages=['cli_anything.aws_redshift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_redshift=cli_anything.aws_redshift:cli']},
)
