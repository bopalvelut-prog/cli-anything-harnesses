from setuptools import setup
setup(
    name='cli-anything-exchange',
    version='1.0.0',
    packages=['cli_anything.exchange'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exchange=cli_anything.exchange:cli']},
)
