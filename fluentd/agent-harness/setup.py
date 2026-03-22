from setuptools import setup
setup(
    name='cli-anything-fluentd',
    version='1.0.0',
    packages=['cli_anything.fluentd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fluentd=cli_anything.fluentd:cli']},
)
