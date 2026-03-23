from setuptools import setup
setup(
    name='cli-anything-otel',
    version='1.0.0',
    packages=['cli_anything.otel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-otel=cli_anything.otel:cli']},
)
