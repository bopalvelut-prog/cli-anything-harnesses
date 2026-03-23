from setuptools import setup
setup(
    name='cli-anything-otelcol',
    version='1.0.0',
    packages=['cli_anything.otelcol'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-otelcol=cli_anything.otelcol:cli']},
)
