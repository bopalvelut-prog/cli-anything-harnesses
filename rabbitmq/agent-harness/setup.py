from setuptools import setup
setup(
    name='cli-anything-rabbitmq',
    version='1.0.0',
    packages=['cli_anything.rabbitmq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rabbitmq=cli_anything.rabbitmq:cli']},
)
