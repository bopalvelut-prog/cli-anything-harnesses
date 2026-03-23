from setuptools import setup
setup(
    name='cli-anything-dapr',
    version='1.0.0',
    packages=['cli_anything.dapr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dapr=cli_anything.dapr:cli']},
)
