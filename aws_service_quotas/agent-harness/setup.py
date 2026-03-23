from setuptools import setup
setup(
    name='cli-anything-aws_service_quotas',
    version='1.0.0',
    packages=['cli_anything.aws_service_quotas'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws_service_quotas=cli_anything.aws_service_quotas:cli']},
)
