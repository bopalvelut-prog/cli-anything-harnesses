from setuptools import setup
setup(
    name='cli-anything-aws_iot_events',
    version='1.0.0',
    packages=['cli_anything.aws_iot_events'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_iot_events=cli_anything.aws_iot_events:cli']},
)
