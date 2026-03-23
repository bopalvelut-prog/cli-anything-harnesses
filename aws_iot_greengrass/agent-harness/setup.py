from setuptools import setup
setup(
    name='cli-anything-aws_iot_greengrass',
    version='1.0.0',
    packages=['cli_anything.aws_iot_greengrass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_iot_greengrass=cli_anything.aws_iot_greengrass:cli']},
)
