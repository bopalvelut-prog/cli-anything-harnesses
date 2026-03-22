from setuptools import setup
setup(
    name='cli-anything-consul',
    version='1.0.0',
    packages=['cli_anything.consul'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-consul=cli_anything.consul:cli']},
)
