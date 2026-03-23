from setuptools import setup
setup(
    name='cli-anything-brightness',
    version='1.0.0',
    packages=['cli_anything.brightness'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brightness=cli_anything.brightness:cli']},
)
