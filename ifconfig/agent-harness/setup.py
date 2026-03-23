from setuptools import setup
setup(
    name='cli-anything-ifconfig',
    version='1.0.0',
    packages=['cli_anything.ifconfig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ifconfig=cli_anything.ifconfig:cli']},
)
