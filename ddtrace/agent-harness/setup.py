from setuptools import setup
setup(
    name='cli-anything-ddtrace',
    version='1.0.0',
    packages=['cli_anything.ddtrace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ddtrace=cli_anything.ddtrace:cli']},
)
