from setuptools import setup
setup(
    name='cli-anything-metabase',
    version='1.0.0',
    packages=['cli_anything.metabase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metabase=cli_anything.metabase:cli']},
)
