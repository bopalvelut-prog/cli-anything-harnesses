from setuptools import setup
setup(
    name='cli-anything-redpanda',
    version='1.0.0',
    packages=['cli_anything.redpanda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redpanda=cli_anything.redpanda:cli']},
)
