from setuptools import setup
setup(
    name='cli-anything-aws_app_mesh',
    version='1.0.0',
    packages=['cli_anything.aws_app_mesh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_app_mesh=cli_anything.aws_app_mesh:cli']},
)
