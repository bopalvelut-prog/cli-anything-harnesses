from setuptools import setup
setup(
    name='cli-anything-province',
    version='1.0.0',
    packages=['cli_anything.province'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-province=cli_anything.province:cli']},
)
