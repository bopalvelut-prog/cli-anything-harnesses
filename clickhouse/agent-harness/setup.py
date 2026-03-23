from setuptools import setup
setup(
    name='cli-anything-clickhouse',
    version='1.0.0',
    packages=['cli_anything.clickhouse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clickhouse=cli_anything.clickhouse:cli']},
)
