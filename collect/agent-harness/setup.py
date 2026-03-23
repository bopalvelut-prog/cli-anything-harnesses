from setuptools import setup
setup(
    name='cli-anything-collect',
    version='1.0.0',
    packages=['cli_anything.collect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-collect=cli_anything.collect:cli']},
)
