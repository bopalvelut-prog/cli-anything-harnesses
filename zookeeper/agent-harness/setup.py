from setuptools import setup
setup(
    name='cli-anything-zookeeper',
    version='1.0.0',
    packages=['cli_anything.zookeeper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zookeeper=cli_anything.zookeeper:cli']},
)
