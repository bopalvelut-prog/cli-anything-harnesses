from setuptools import setup
setup(
    name='cli-anything-insight',
    version='1.0.0',
    packages=['cli_anything.insight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-insight=cli_anything.insight:cli']},
)
