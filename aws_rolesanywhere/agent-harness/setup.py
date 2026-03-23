from setuptools import setup
setup(
    name='cli-anything-aws_rolesanywhere',
    version='1.0.0',
    packages=['cli_anything.aws_rolesanywhere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_rolesanywhere=cli_anything.aws_rolesanywhere:cli']},
)
