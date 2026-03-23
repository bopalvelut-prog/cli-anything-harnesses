from setuptools import setup
setup(
    name='cli-anything-fluentbit',
    version='1.0.0',
    packages=['cli_anything.fluentbit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fluentbit=cli_anything.fluentbit:cli']},
)
