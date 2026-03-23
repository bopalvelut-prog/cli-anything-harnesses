from setuptools import setup
setup(
    name='cli-anything-snowflake',
    version='1.0.0',
    packages=['cli_anything.snowflake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-snowflake=cli_anything.snowflake:cli']},
)
