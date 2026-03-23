from setuptools import setup
setup(
    name='cli-anything-activemq',
    version='1.0.0',
    packages=['cli_anything.activemq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activemq=cli_anything.activemq:cli']},
)
