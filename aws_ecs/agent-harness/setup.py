from setuptools import setup
setup(
    name='cli-anything-aws_ecs',
    version='1.0.0',
    packages=['cli_anything.aws_ecs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_ecs=cli_anything.aws_ecs:cli']},
)
