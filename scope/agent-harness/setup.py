from setuptools import setup
setup(
    name='cli-anything-scope',
    version='1.0.0',
    packages=['cli_anything.scope'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scope=cli_anything.scope:cli']},
)
