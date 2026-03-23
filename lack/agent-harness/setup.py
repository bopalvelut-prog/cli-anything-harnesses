from setuptools import setup
setup(
    name='cli-anything-lack',
    version='1.0.0',
    packages=['cli_anything.lack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lack=cli_anything.lack:cli']},
)
