from setuptools import setup
setup(
    name='cli-anything-oak',
    version='1.0.0',
    packages=['cli_anything.oak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oak=cli_anything.oak:cli']},
)
