from setuptools import setup
setup(
    name='cli-anything-sender',
    version='1.0.0',
    packages=['cli_anything.sender'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sender=cli_anything.sender:cli']},
)
