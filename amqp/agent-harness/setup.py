from setuptools import setup
setup(
    name='cli-anything-amqp',
    version='1.0.0',
    packages=['cli_anything.amqp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amqp=cli_anything.amqp:cli']},
)
