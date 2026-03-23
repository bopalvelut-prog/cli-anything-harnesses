from setuptools import setup
setup(
    name='cli-anything-aws_elasticache',
    version='1.0.0',
    packages=['cli_anything.aws_elasticache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_elasticache=cli_anything.aws_elasticache:cli']},
)
