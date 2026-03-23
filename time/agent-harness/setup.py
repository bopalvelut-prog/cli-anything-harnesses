from setuptools import setup
setup(
    name='cli-anything-time',
    version='1.0.0',
    packages=['cli_anything.time'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-time=cli_anything.time:cli']},
)
