from setuptools import setup
setup(
    name='cli-anything-reuse',
    version='1.0.0',
    packages=['cli_anything.reuse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reuse=cli_anything.reuse:cli']},
)
