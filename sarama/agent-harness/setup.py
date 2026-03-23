from setuptools import setup
setup(
    name='cli-anything-sarama',
    version='1.0.0',
    packages=['cli_anything.sarama'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sarama=cli_anything.sarama:cli']},
)
