from setuptools import setup
setup(
    name='cli-anything-confluent',
    version='1.0.0',
    packages=['cli_anything.confluent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-confluent=cli_anything.confluent:cli']},
)
