from setuptools import setup
setup(
    name='cli-anything-presence',
    version='1.0.0',
    packages=['cli_anything.presence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-presence=cli_anything.presence:cli']},
)
