from setuptools import setup
setup(
    name='cli-anything-nsq',
    version='1.0.0',
    packages=['cli_anything.nsq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nsq=cli_anything.nsq:cli']},
)
