from setuptools import setup
setup(
    name='cli-anything-engine',
    version='1.0.0',
    packages=['cli_anything.engine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-engine=cli_anything.engine:cli']},
)
