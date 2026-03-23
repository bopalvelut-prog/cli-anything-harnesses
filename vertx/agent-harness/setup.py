from setuptools import setup
setup(
    name='cli-anything-vertx',
    version='1.0.0',
    packages=['cli_anything.vertx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vertx=cli_anything.vertx:cli']},
)
