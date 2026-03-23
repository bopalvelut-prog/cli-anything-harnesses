from setuptools import setup
setup(
    name='cli-anything-aws_iot_sitewise',
    version='1.0.0',
    packages=['cli_anything.aws_iot_sitewise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_iot_sitewise=cli_anything.aws_iot_sitewise:cli']},
)
