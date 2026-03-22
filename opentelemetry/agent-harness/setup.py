from setuptools import setup
setup(
    name='cli-anything-opentelemetry',
    version='1.0.0',
    packages=['cli_anything.opentelemetry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opentelemetry=cli_anything.opentelemetry:cli']},
)
