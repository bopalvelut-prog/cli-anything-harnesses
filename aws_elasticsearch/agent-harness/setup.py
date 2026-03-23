from setuptools import setup
setup(
    name='cli-anything-aws_elasticsearch',
    version='1.0.0',
    packages=['cli_anything.aws_elasticsearch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_elasticsearch=cli_anything.aws_elasticsearch:cli']},
)
