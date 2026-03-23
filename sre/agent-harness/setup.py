from setuptools import setup
setup(
    name='cli-anything-sre',
    version='1.0.0',
    packages=['cli_anything.sre'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sre=cli_anything.sre:cli']},
)
