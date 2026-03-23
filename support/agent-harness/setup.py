from setuptools import setup
setup(
    name='cli-anything-support',
    version='1.0.0',
    packages=['cli_anything.support'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-support=cli_anything.support:cli']},
)
