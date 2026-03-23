from setuptools import setup
setup(
    name='cli-anything-aws_opsworks',
    version='1.0.0',
    packages=['cli_anything.aws_opsworks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_opsworks=cli_anything.aws_opsworks:cli']},
)
