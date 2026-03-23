from setuptools import setup
setup(
    name='cli-anything-hono',
    version='1.0.0',
    packages=['cli_anything.hono'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hono=cli_anything.hono:cli']},
)
