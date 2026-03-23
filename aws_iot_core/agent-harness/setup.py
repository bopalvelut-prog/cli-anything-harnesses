from setuptools import setup
setup(
    name='cli-anything-aws_iot_core',
    version='1.0.0',
    packages=['cli_anything.aws_iot_core'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_iot_core=cli_anything.aws_iot_core:cli']},
)
