from setuptools import setup
setup(
    name='cli-anything-grpc',
    version='1.0.0',
    packages=['cli_anything.grpc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grpc=cli_anything.grpc:cli']},
)
