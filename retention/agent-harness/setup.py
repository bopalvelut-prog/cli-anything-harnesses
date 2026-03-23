from setuptools import setup
setup(
    name='cli-anything-retention',
    version='1.0.0',
    packages=['cli_anything.retention'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retention=cli_anything.retention:cli']},
)
