from setuptools import setup
setup(
    name='cli-anything-aws_service_catalog',
    version='1.0.0',
    packages=['cli_anything.aws_service_catalog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_service_catalog=cli_anything.aws_service_catalog:cli']},
)
