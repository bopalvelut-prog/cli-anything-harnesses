from setuptools import setup
setup(
    name='cli-anything-stackstorm',
    version='1.0.0',
    packages=['cli_anything.stackstorm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stackstorm=cli_anything.stackstorm:cli']},
)
