from setuptools import setup
setup(
    name='cli-anything-bus',
    version='1.0.0',
    packages=['cli_anything.bus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bus=cli_anything.bus:cli']},
)
