from setuptools import setup
setup(
    name='cli-anything-aws_neptune',
    version='1.0.0',
    packages=['cli_anything.aws_neptune'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_neptune=cli_anything.aws_neptune:cli']},
)
