from setuptools import setup
setup(
    name='cli-anything-elasticmq',
    version='1.0.0',
    packages=['cli_anything.elasticmq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elasticmq=cli_anything.elasticmq:cli']},
)
