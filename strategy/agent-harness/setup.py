from setuptools import setup
setup(
    name='cli-anything-strategy',
    version='1.0.0',
    packages=['cli_anything.strategy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strategy=cli_anything.strategy:cli']},
)
