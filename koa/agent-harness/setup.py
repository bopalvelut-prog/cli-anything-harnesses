from setuptools import setup
setup(
    name='cli-anything-koa',
    version='1.0.0',
    packages=['cli_anything.koa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-koa=cli_anything.koa:cli']},
)
