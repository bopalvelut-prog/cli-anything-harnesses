from setuptools import setup
setup(
    name='cli-anything-dbt',
    version='1.0.0',
    packages=['cli_anything.dbt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dbt=cli_anything.dbt:cli']},
)
