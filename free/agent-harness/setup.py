from setuptools import setup
setup(
    name='cli-anything-free',
    version='1.0.0',
    packages=['cli_anything.free'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-free=cli_anything.free:cli']},
)
