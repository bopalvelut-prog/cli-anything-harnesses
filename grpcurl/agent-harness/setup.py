from setuptools import setup
setup(
    name='cli-anything-grpcurl',
    version='1.0.0',
    packages=['cli_anything.grpcurl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grpcurl=cli_anything.grpcurl:cli']},
)
