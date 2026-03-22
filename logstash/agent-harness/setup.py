from setuptools import setup
setup(
    name='cli-anything-logstash',
    version='1.0.0',
    packages=['cli_anything.logstash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logstash=cli_anything.logstash:cli']},
)
