from setuptools import setup
setup(
    name='cli-anything-reset',
    version='1.0.0',
    packages=['cli_anything.reset'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reset=cli_anything.reset:cli']},
)
