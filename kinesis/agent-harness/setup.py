from setuptools import setup
setup(
    name='cli-anything-kinesis',
    version='1.0.0',
    packages=['cli_anything.kinesis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kinesis=cli_anything.kinesis:cli']},
)
