from setuptools import setup
setup(
    name='cli-anything-impala',
    version='1.0.0',
    packages=['cli_anything.impala'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-impala=cli_anything.impala:cli']},
)
