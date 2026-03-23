from setuptools import setup
setup(
    name='cli-anything-partitions',
    version='1.0.0',
    packages=['cli_anything.partitions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-partitions=cli_anything.partitions:cli']},
)
