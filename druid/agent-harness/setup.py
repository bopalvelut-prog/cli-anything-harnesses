from setuptools import setup
setup(
    name='cli-anything-druid',
    version='1.0.0',
    packages=['cli_anything.druid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-druid=cli_anything.druid:cli']},
)
