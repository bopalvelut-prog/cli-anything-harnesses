from setuptools import setup
setup(
    name='cli-anything-aws_systems_manager',
    version='1.0.0',
    packages=['cli_anything.aws_systems_manager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_systems_manager=cli_anything.aws_systems_manager:cli']},
)
