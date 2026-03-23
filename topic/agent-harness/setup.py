from setuptools import setup
setup(
    name='cli-anything-topic',
    version='1.0.0',
    packages=['cli_anything.topic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-topic=cli_anything.topic:cli']},
)
